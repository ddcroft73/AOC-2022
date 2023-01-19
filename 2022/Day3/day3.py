import os 
fpath: str = os.getcwd() + '/2022/Day3/input.txt'

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

    def find_common_type(str1: str, str2: str) -> str:
        '''
        Given two strings of equal length, find the common char between los dos!
        Case sensitive.
        '''
        for char in str1:
            if (char in str2):  
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
    
    with open(fpath, 'r') as f:
        back_packs: list[str] = f.readlines()
        for back_pack in back_packs:
            pack1, pack2 = split_back_packs(back_pack)
            item_type: str = find_common_type(pack1, pack2)
            type_priority += assign_priority(item_type)

    return type_priority



# There is no error checking in any of these routines. The assumption is all input is accurate
# I basically just hone in on the instructions and consume the input with them in mind. Should 
# there be error chceking even in this circumstance? 
def main() -> None:
    priority_sum: int = reorganize_back_packs()
    print(f'The sum of the priorities of the back packs is: [ {priority_sum} ]')
    


if __name__ == "__main__":
    main()
