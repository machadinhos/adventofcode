import shutil
from collections.abc import Generator
from multiprocessing import Pool, cpu_count
from pathlib import Path
from time import perf_counter

from utils import get_next_str, load_data


def generate_and_save_after_n_iter(num: str, iterations: list[int]) -> None:
    i_list = [num]
    if 1 in iterations:
        i_str = " ".join([new_num for num in i_list for new_num in get_next_str(num)])
        Path(f"helper/nums_after_1/{num}.txt").write_text(i_str)
    for i in range(1, max(iterations) + 1):
        i_list = [new_num for num in i_list for new_num in get_next_str(num)]
        if i in iterations:
            i_str = " ".join(i_list)
            Path(f"helper/nums_after_{i}/{num}.txt").write_text(i_str)


def handle_chunks(chunk: list[str], iterations: list[int]) -> None:
    for num in chunk:
        generate_and_save_after_n_iter(num, iterations)


def chunk_list_for_cpus(num_list: list[str]):
    num_cpus = cpu_count()
    num_items = len(num_list)

    if num_cpus >= num_items:
        return [[item] for item in num_list]

    base_chunk_size = num_items // num_cpus
    remainder = num_items % num_cpus

    chunks = []
    start_idx = 0
    for i in range(num_cpus):
        chunk_size = base_chunk_size + (1 if i < remainder else 0)
        chunks.append(num_list[start_idx : start_idx + chunk_size])
        start_idx += chunk_size

    return chunks


def main(future_iterations: list[int] | int, range_to_include: int, clear_helper_folder=False):
    if type(future_iterations) is int:
        future_iterations = [future_iterations]
    for i in future_iterations:
        path = Path(f"helper/nums_after_{i}/")
        if clear_helper_folder and path.exists() and path.is_dir():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)

    print("starting range to include calculation...")
    start = perf_counter()
    i_list = load_data()
    unique = set(i_list)
    for _ in range(range_to_include):
        i_list = [new_num for num in i_list for new_num in get_next_str(num)]
        unique.update(i_list)
    end = perf_counter()
    print(f"it took {end - start}s to calculate the range to include")

    print("number of unique nums to include:", len(unique))
    l_data = list(unique)

    input_data: Generator[(list[str], list[int])] = (
        (chunk, future_iterations) for chunk in chunk_list_for_cpus(l_data)
    )

    print("starting pool...")
    start = perf_counter()
    with Pool() as pool:
        pool.starmap(handle_chunks, input_data)
    end = perf_counter()
    print(f"it took {end - start}s to process all data")
    print("done")


if __name__ == "__main__":
    # CAREFUL THIS USES ALL YOUR SYSTEM RESOURCES, CAN TAKE A WHILE TO RUN AND CAN OCCUPIES A LOT OF DISK SPACE
    main(37, 35)
