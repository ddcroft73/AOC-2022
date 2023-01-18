
# open and read the file
# split each rucksack in half
# find te common upper or lowercase char 
# convert the types into a priority, (ie. All lower case chars are assigned a numerical value 1 -26 respectively
#                                     and all Upper are asssigned 27 - 52)
#add up the priorites

import os 
fpath: str = os.getcwd() + '/2022/Day3/input.txt'


def reorganize_back_packs() -> int:
    type_priority: int = 0

    def split_back_packs(bp: str) -> tuple[str]:
        bp = bp.strip()
        both_pack_len: int = int(len(bp) / 2)

        return (
            bp[:both_pack_len],
            bp[both_pack_len:]
        )


    def find_common_type(str1: str, str2: str) -> str:
        '''
        Given two strings of equal length, find the common char between the 2.
        Case sensitive.
        '''
        for char in str1:
            if (char in str2):  # hehe python
                item_type: str = char
                break
        return item_type


    def assign_priority(item: str) -> int:
        '''
        Given the 'type', assign it a value to be used later in assessing value.
        '''
        lower_offset: int = 96
        upper_offset: int = 38
        priority: int = 0

        if (item.isupper()):
            priority = ord(item) - upper_offset
        if (item.islower()):
            priority = ord(item) - lower_offset
        return priority    

    
    with open(fpath, 'r') as f:
        back_packs: list[str] = f.readlines()
        for back_pack in back_packs:
            pack1, pack2 = split_back_packs(back_pack)
            item_type: str = find_common_type(pack1, pack2)
            type_priority += assign_priority(item_type)

    return type_priority


def main() -> None:
    result: int = reorganize_back_packs()
    print(result)
    

# zgzVNHHg and MwMLbLNB is:: N


if __name__ == "__main__":
    main()
