import itertools
import multiprocessing

possible_digits = '0123456789'
password_length = 10

# Define a function to generate passwords and write them to a file
def generate_passwords(start, end, filename):
    with open(filename, 'a') as file:
        for password in itertools.product(possible_digits, repeat=password_length):
            password_str = ''.join(password)
            print(password_str)

if __name__ == '__main__':
    # Get the number of CPU cores available
    num_cores = multiprocessing.cpu_count()

    # Split the password generation task into equal chunks for each core
    chunk_size = len(possible_digits) ** password_length // num_cores
    chunks = [(i * chunk_size, (i+1) * chunk_size, 'passwords.txt') for i in range(num_cores)]

    # Start a separate process for each core
    processes = []
    for start, end, filename in chunks:
        p = multiprocessing.Process(target=generate_passwords, args=(start, end, filename))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()
