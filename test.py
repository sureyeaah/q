import json
import os
from multiprocessing import Pool

import numpy as np

from tasks import TEST_DATA_PATH


def verify(prefix):
  print(f"Verifying prefix: {prefix}")
  # Read all the files one by one and calculate the average per index.
  path = os.path.join(TEST_DATA_PATH, prefix)

  # files have the name random_numbers_{i}.txt
  files = [
      os.path.join(path, file)
      for file in os.listdir(path)
      if "random_numbers" in file
  ]

  # Read all the files and calculate the average per index and write it to a new file
  average = []
  count = 0
  for file in files:
    print(f"Reading file: {file}")
    with open(file, "r") as f:
      file_data = json.loads(f.read())
      data = np.array(file_data['data'])
      if count == 0:
        average = data
      else:
        average = np.add(average, data)
      count += 1

  average = np.divide(average, count)
  # Find the file in the directory with output_{count} in the name
  received_output_file_name = [
      file for file in os.listdir(path) if f"output_{count}" in file
  ][0]

  received_average = []
  # Read the file and compare the data
  with open(os.path.join(path, received_output_file_name), "r") as f:
    received_output = json.loads(f.read())
    received_average = np.array(received_output['data'])

  # Compare the data
  # There's should be an error of < 1e-15
  assert np.allclose(average, received_average, atol=1e-15)
  print(f"Test passed for prefix: {prefix} with {count} files")


if __name__ == "__main__":
  # Get all the prefixes. They are in the TEST_DATA_PATH folder
  prefixes = [
      file for file in os.listdir(TEST_DATA_PATH)
      if os.path.isdir(os.path.join(TEST_DATA_PATH, file))
  ]
  pool = Pool(processes=4)
  pool.map(verify, prefixes)
