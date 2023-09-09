""" 
job_queue.py

"""


from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class JobQueue:
    """
    Create a Job Queue Object

    """

    def __init__(self, num_workers, jobs):
        self.num_workers = num_workers
        self.jobs = jobs
        self.finish_time_list = []
        self.assigned_jobs_list = []
        for i in range(self.num_workers):
            self.finish_time_list.append([i, 0])

    def left_child(self, index):
        """
        Return the index of the left side child node given the index of the parent node.

        Args:
            index (int): Parent node index

        Returns:
            int: Index of the left child node

        """
        return 2 * index + 1

    def right_child(self, index):
        """
        Return the index of the right side child node given the index of the parent node.

        Args:
            index (int): Parent node index

        Returns:
            int: Index of the right child node

        """
        return 2 * index + 2

    def sift_down(self, index):
        """
        Sift an element in a binary tree down recursively.

        Args:
            index (int): Index of the element to sift down

        """
        min_index = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < self.num_workers:
            if self.finish_time_list[min_index][1] > self.finish_time_list[left][1]:
                min_index = left
            elif self.finish_time_list[min_index][1] == self.finish_time_list[left][1]:
                if self.finish_time_list[min_index][0] > self.finish_time_list[left][0]:
                    min_index = left

        if right < self.num_workers:
            if self.finish_time_list[min_index][1] > self.finish_time_list[right][1]:
                min_index = right
            elif self.finish_time_list[min_index][1] == self.finish_time_list[right][1]:
                if (
                    self.finish_time_list[min_index][0]
                    > self.finish_time_list[right][0]
                ):
                    min_index = right

        if min_index != index:
            self.finish_time_list[index], self.finish_time_list[min_index] = (
                self.finish_time_list[min_index],
                self.finish_time_list[index],
            )

            self.sift_down(min_index)

    def next_worker(self, job):
        """
        Assign a job to the next worker and update the finish times list.

        Args:
            job (int): Job Number

        """
        root = self.finish_time_list[0]
        next_worker = root[0]
        started_at = root[1]
        self.assigned_jobs_list.append(AssignedJob(next_worker, started_at))
        self.finish_time_list[0][1] += job
        self.sift_down(0)


def main():
    """
    Main method

    """
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    job_queue = JobQueue(n_workers, jobs)
    for job in jobs:
        job_queue.next_worker(job)
    assigned_jobs = job_queue.assigned_jobs_list

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
