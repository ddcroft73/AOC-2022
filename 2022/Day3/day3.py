import os 
fpath: str = os.getcwd() + '/2022/Day3/input.txt'


def find_common_itemType(*strings: tuple[str]) -> str:
    '''
    Given two or three strings of equal or differing length,
    find the common char between them!
    Case sensitive.

    Want to tighten this up make it so it doesnt matter how many strings are passed in.
    Pretty basic.... expand on this
    '''
    if (len(strings) == 2):
        for char in strings[0]:
            if (char in strings[1]):
                item_type: str = char
                break
    elif (len(strings) == 3):
        for char in strings[0]:
            if ((char in strings[1]) and (char in strings[2])):
                item_type: str = char
                break
    return item_type

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
        '''Name pretty much sez it....'''
        bp = bp.strip()
        both_pack_len: int = int(len(bp) / 2) # assumes they are all divisible by 2

        return (
            bp[: both_pack_len],
            bp[both_pack_len :]
        )    

    with open(fpath, 'r') as f:
        back_packs: list[str] = f.readlines()[:1]

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
        if (elf_cnt+1) % 3 == 0 and elf_cnt != 0: 
            # get the badge type of the 3
            item_type: str = find_common_itemType(*elf_group)
            type_priority += assign_priority(item_type)
            # next...
            elf_group = []

    return type_priority


def main() -> None:
    priority_sum_ruckSacks: int = reorganize_back_packs()
    priority_sum_badges: int = prioritize_group_badges()

    print(
        f'The sum of the priorities of the back packs is: [ {priority_sum_ruckSacks} ]')
    print(
        f'The sum of the priorities of Elves badges is: [ {priority_sum_badges} ]')


if __name__ == "__main__":
    main()


"""
        # count all the chars in the string.
        for letter in (str_joined):
            char[letter] = str_joined.count(letter)"""
