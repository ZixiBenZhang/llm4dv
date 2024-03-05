from dataclasses import dataclass
from typing import Optional, List, Tuple
from pprint import pprint

@dataclass
class Stimulus:
    value: Optional[List]
    finish: bool

@dataclass
class DUTState:
    allocated_nodeslot: int

    def state_vector(self):
        return [
            self.allocated_nodeslot
        ]
    
class CoverageDatabase:
    # adj_dealloc: int
    # mess_dealloc: int
    # scale_dealloc: int

    # adj_nomatch: int
    # mess_nomatch: int
    # scale_nomatch: int

    # mess_fetch_adj_nopartial: int
    # mess_fetch_adj_partial: int
    
    # mess_nopartial: int
    # mess_partial: int

    # scale_nopartial: int
    # scale_partial: int

    misc_bins: dict[str, int]


"""
Operations:
-Allocate/deallocate tag
-Fetch adjacency list
-Fetch messages
-Fetch scale factors

BIN LIST:
-Operations when tag is deallocated
-Operations when nodeslots do not match
-Message fetch with non-partial/partial adj queue
-Message fetch non-partial/partial
-Scale fetch non-partial/partial
"""