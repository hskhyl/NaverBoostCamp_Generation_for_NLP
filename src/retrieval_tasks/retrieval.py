from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union, NoReturn

class retrieval:
    @abstractmethod
    def __init__(
        self,
        tokenize_fn,
        dense_model_name: list,
        data_path: Optional[str],
        context_path: Optional[str],
    ) -> NoReturn:
        pass  
    
    @abstractmethod
    def retrieve(self, query_or_dataset, topk: Optional[int], alpha: Optional[float], no_sparse: bool):
        pass