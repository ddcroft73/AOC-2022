import os 
from typing import Any
# No error checking whatsoever.... erks me not to do so.. but I don't guess it matters when the constraints are so precise.

fpath: str = os.getcwd() + '/2022/Day3/input.txt'


def find_common_itemType(*args: tuple[Any]) -> str:
    '''
     Uses set intersection to find any common items between multiple arrays\lists\iterables.
    '''
    set_list: list[Any] = [set(arg) for arg in args]
    common_item_set: set[Any] = set_list[0].intersection(*set_list)    
    return "".join(common_item_set)
    

def assign_priority(item: str) -> int:
    '''
    Given the 'type', assign it a value to be used later in asscessing... well,  value.
    '''
    lower_offset: int = 96
    upper_offset: int = 38
    priority: int = 0

    if (item.isupper()):
        priority = ord(item) - upper_offset
    if (item.islower()):
        priority = ord(item) - lower_offset
    return priority    
    


def reorganize_back_packs() -> int:
    type_priority: int = 0

    def split_back_packs(bp: str) -> tuple[str]:
        bp = bp.strip()
        both_pack_len: int = int(len(bp) / 2) 

        return (
            bp[: both_pack_len],
            bp[both_pack_len :]
        )    

    with open(fpath, 'r') as f:
        back_packs: list[str] = f.readlines()

        for back_pack in back_packs:
            pack1, pack2 = split_back_packs(back_pack)
            item_type: str = find_common_itemType(pack1, pack2)
            type_priority += assign_priority(item_type)

    return type_priority


def prioritize_group_badges():
    elf_group: list[str] = []
    type_priority: int = 0
    
    with open(fpath, 'r') as f:
        elf_population: list[str] = f.readlines()
        elf_population = [line.strip() for line in elf_population]
    
    for elf_cnt, elf in enumerate(elf_population):
        elf_group.append(elf)
        
        # cull the elves into groups of three for processing, 
        if ((elf_cnt+1) % 3 == 0): 
            item_type: str = find_common_itemType(*elf_group)
            type_priority += assign_priority(item_type)
            elf_group = []

    return type_priority


def main() -> None:
    priority_sum_ruckSacks: int = reorganize_back_packs()
    priority_sum_badges: int = prioritize_group_badges()

    print(f'The sum of the priorities of the back packs is: [ {priority_sum_ruckSacks} ]')
    print(f'The sum of the priorities of Elves badges is: [ {priority_sum_badges} ]')


if __name__ == "__main__":
    main()
