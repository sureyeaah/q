- Design a system that assigns a task to a fleet of workers, the worker's outputs are aggregated into a single result which is returned to the user.
- The task itself will be to use at most W workers to compute the mean of every index across files of numbers, where F is the number of files, and each file contains C random numbers. So if F=2 and C=3, and the input files are [1,2,3] and [4,5,6] then the output file will be [2.5, 3.5, 4.5]. Values for W, F, and C should all be chosen by the user. For the random numbers themselves, feel free to put whatever bound you want on them (between 0 and 1 for example). Files can use a format of your choice (csv, etc).
- How would you design metrics around the performance of your system?
- pip install numpy flask redis celery
