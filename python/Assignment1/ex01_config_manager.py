import json
import os

if __name__ == "__main__":

    config = {
        "job_name": "matrix_benchmark",
        "num_workers": 4,
        "chunk_size": 1000,
        "timeout_sec": 30.0,
        "retry_on_failure": True,
        "input_files": [
            "data_part1.csv",
            "data_part2.csv",
            "data_part3.csv"
        ]
    }
    print(config)



    # Save this configuration to a file called job_config.json

    with open('job_config.json', 'w') as file:
        json.dump(config,file,indent=4)
        print("file written successfully. \n")

    # Load the configuration back from the file.
    with open('job_config.json', 'r') as file:
        print(json.load(file))
        print("read from json file successfully.\n")


    # Modify  a value (e.g., change num_workers to 8) and save it again.
    config['num_workers'] = 8
    with open("job_config.json",'w') as file:
        json.dump(config, file, indent=4)


    with open('job_config.json', 'r') as file:
        restored = json.load(file)
        print("\nRestored = ",restored)
        print("read from json file successfully.")





