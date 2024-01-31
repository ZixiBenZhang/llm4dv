# Copyright Zixi Zhang
# Licensed under the Apache License, Version 2.0, see LICENSE for details.
# SPDX-License-Identifier: Apache-2.0

import re
from abc import abstractmethod
from typing import List, Tuple, Optional


class BaseExtractor:
    @abstractmethod
    def __call__(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError


class DumbExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()

    def __call__(self, text: str) -> List[int]:
        literals = list(
            re.findall(r"(?:0x[\da-fA-F]+)|(?:-?\d+(?!\d)(?!\.)(?!:))", text, re.I)
        )
        numbers = list(
            map(lambda x: (int(x, 16) if x[:2] == "0x" else int(x)), literals)
        )
        return numbers

    def reset(self):
        pass

class AG_WBExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()
    # (a,b),(c,d),(e,f)
    def __call__(self, text: str) -> List[Tuple[int, int]]:
        stimuli = []
        stim_str = text.replace("(", "").replace(")", "").replace("[", "").replace("]", "").split(",")
        i = 0
        while (i < len(stim_str)-1):
            stimuli.append([int(stim_str[i]), int(stim_str[i+1])])
            i += 2
        return stimuli
    
    def reset(self):
        pass

class ICExtractor(BaseExtractor):
    def __init__(self):
        super().__init__()

    def __call__(self, text: str) -> List[Tuple[int, int]]:
        pairs: List[str] = list(
            re.findall(r"\(\"?'?0x[\da-fA-F]+'?\"?, ?\"?'?0x[\da-fA-F]+'?\"?\)", text, re.I)
        )
        updates = list(
            map(
                lambda t: tuple(map(
                    lambda x: int(x, 16), t[1:-1].replace("'", "").replace('"', '').split(",")
                ))[:2],
                pairs,
            )
        )
        return updates

    def reset(self):
        pass
