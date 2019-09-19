from typing import Callable, Union

from kgforge.core.commons.typing import DirPath, FilePath, Hjson, URL
from kgforge.core.modeling import ModelingInterface
from kgforge.core.modeling.handlers import FilesHandler, IdentifiersHandler, OntologiesHandler
from kgforge.core.querying import QueryingInterface
from kgforge.core.storing import Store, StoringInterface
from kgforge.core.transforming import TransformingInterface


class KnowledgeGraphForge:

    # FIXME Implement cases where some of the arguments can be optional.
    def __init__(self, model: Callable, schemas: Union[DirPath, URL, Store],
                 store: Callable, files_mapping: Union[Hjson, FilePath, URL], bucket: str, token: str,
                 ontologies: Union[DirPath, URL, Store], ontologies_mapping: Union[Hjson, FilePath, URL],
                 identifiers_formatter: str) -> None:
        self.model = model(schemas)
        self.store = store(files_mapping, bucket, token)
        # Handlers.
        self.ontologies = OntologiesHandler(ontologies, ontologies_mapping)
        self.identifiers = IdentifiersHandler(identifiers_formatter)
        self.files = FilesHandler(self)
        # Interfaces.
        self.modeling = ModelingInterface(self.model)
        self.storing = StoringInterface(self.store)
        self.querying = QueryingInterface(self)
        self.transforming = TransformingInterface(self)

    @staticmethod
    def from_config(path: str, bucket: str, token: str) -> "KnowledgeGraphForge":
        # The configuration file is in YAML.
        # FIXME Implement.
        raise NotImplementedError