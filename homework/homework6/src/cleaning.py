from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple, Dict

import numpy as np
import pandas as pd


__all__ = [
    "fill_missing_median",
    "drop_missing",
    "normalize_data",
    "NormalizationParams",
]


@dataclass
class NormalizationParams:
    columns: List[str]
    method: str  # 'zscore' or 'minmax'
    params: Dict[str, Dict[str, float]]  # per-column stats


def _infer_numeric_columns(df: pd.DataFrame, columns: Optional[Iterable[str]]) -> List[str]:
    if columns is None:
        return df.select_dtypes(include=[np.number]).columns.tolist()
    return [c for c in columns if c in df.columns]


def fill_missing_median(
    df: pd.DataFrame,
    columns: Optional[Iterable[str]] = None,
    by: Optional[Iterable[str]] = None,
) -> pd.DataFrame:
    
    out = df.copy()
    cols = _infer_numeric_columns(out, columns)

    if not cols:
        return out

    if by is None:
        medians = out[cols].median(numeric_only=True)
        out[cols] = out[cols].fillna(medians)
    else:
        for col in cols:
            med = out.groupby(list(by))[col].transform(lambda s: s.median(skipna=True))
            out[col] = out[col].fillna(med)
        remaining_na = [c for c in cols if out[c].isna().any()]
        if remaining_na:
            global_medians = out[remaining_na].median(numeric_only=True)
            out[remaining_na] = out[remaining_na].fillna(global_medians)
    return out


def drop_missing(
    df: pd.DataFrame,
    row_thresh: float = 0.5,
    col_thresh: float = 0.5,
) -> pd.DataFrame:
    out = df.copy()

    col_na_frac = out.isna().mean(axis=0)
    keep_cols = col_na_frac[col_na_frac <= col_thresh].index
    out = out[keep_cols]

    if out.shape[1] > 0:
        row_na_frac = out.isna().mean(axis=1)
        out = out.loc[row_na_frac <= row_thresh].copy()
    else:
        out = out.iloc[0:0]

    return out


def normalize_data(
    df: pd.DataFrame,
    columns: Optional[Iterable[str]] = None,
    method: str = "zscore",
    exclude: Optional[Iterable[str]] = None,
    clip_quantiles: Optional[Tuple[float, float]] = None,
) -> Tuple[pd.DataFrame, NormalizationParams]:
    
    out = df.copy()
    cols = _infer_numeric_columns(out, columns)
    if exclude is not None:
        cols = [c for c in cols if c not in set(exclude)]

    if not cols:
        return out, NormalizationParams(columns=[], method=method, params={})

    params: Dict[str, Dict[str, float]] = {}

    for c in cols:
        series = out[c].astype(float)

        if clip_quantiles is not None:
            lo, hi = clip_quantiles
            qlo, qhi = series.quantile([lo, hi])
            series = series.clip(lower=qlo, upper=qhi)

        if method == "zscore":
            mean = float(series.mean())
            std = float(series.std(ddof=0))  
            if std == 0.0:
                out[c] = series - mean
                params[c] = {"mean": mean, "std": 0.0}
            else:
                out[c] = (series - mean) / std
                params[c] = {"mean": mean, "std": std}
        elif method == "minmax":
            vmin = float(series.min())
            vmax = float(series.max())
            rng = vmax - vmin
            if rng == 0.0:
                out[c] = 0.0  
                params[c] = {"min": vmin, "max": vmax}
            else:
                out[c] = (series - vmin) / rng
                params[c] = {"min": vmin, "max": vmax}
        else:
            raise ValueError("method must be 'zscore' or 'minmax'")

    norm_params = NormalizationParams(columns=cols, method=method, params=params)
    return out, norm_params

