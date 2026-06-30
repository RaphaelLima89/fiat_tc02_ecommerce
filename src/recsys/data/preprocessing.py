from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class PreprocessingStrategy(ABC):
    """Interface para estratégias de pré-processamento."""

    @abstractmethod
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Transforma os dados de entrada.

        Args:
            data (pd.DataFrame): Dados de entrada a serem transformados.

        Returns:
            pd.DataFrame: Dados transformados.
        """
        raise NotImplementedError


class SessionAggregationStrategy(PreprocessingStrategy):
    """Estratégia de agregação de sessões."""

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Estratégia de agregação de sessões não implementada ainda.")
