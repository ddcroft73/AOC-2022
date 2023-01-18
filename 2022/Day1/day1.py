
import os
fpath: str = os.getcwd() + '/2022/Day1/input.txt'

def generate_calorie_list(path: str) -> list[int]:
    elf_cache: list[int] = []
    food: int = 0

    with open(path, 'r') as file:
        lines: list[str] = file.readlines()
        for line in lines:
            if (line.strip()):
                food += int(line)
            else:
                elf_cache.append(food)
                food = 0
    return elf_cache


def main() -> None:    
    calorie_list: list[int] = generate_calorie_list(fpath)
    largest_holder: int = max(calorie_list)
    total_top_three: int = sum(sorted(calorie_list)[-3:])

    print(f"Calories rounded-up. The largest holder is: {largest_holder}")
    print(sorted(calorie_list)[-3:])
    print(f"The total of the top three calorie holders's: {total_top_three}")


if __name__ == "__main__":
    main()
