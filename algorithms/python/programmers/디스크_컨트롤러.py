# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq


class Job:
    remaining_time = None
    requested_time = None
    is_finished = False

    def __init__(self, requested_time, processing_time):
        self.remaining_time = processing_time
        self.requested_time = requested_time

    def tick(self):
        self.remaining_time -= 1
        if self.remaining_time == 0:
            self.is_finished = True

    def __gt__(self, other):
        return self.remaining_time > other.remaining_time

    def __lt__(self, other):
        return self.remaining_time < other.remaining_time


class Processor:
    job_count = 0
    current_job = None
    jobs = []
    timer = 0
    processing_time_summed = 0

    def tick(self):
        self.timer += 1
        if not self.current_job:
            if self.jobs:
                _, self.current_job = heapq.heappop(self.jobs)
            else:
                return

        self.current_job.tick()
        if self.current_job.is_finished:
            self.processing_time_summed += (
                self.timer - self.current_job.requested_time
            )
            self.current_job = None

    def attatch_job(self, job):
        self.job_count += 1
        heapq.heappush(
            self.jobs, (job.remaining_time, job)
        )


def solution(jobs):
    if not jobs:
        return 0

    jobs.sort(key=lambda x: x[0])
    processor = Processor()

    timer = 0
    while jobs:
        while jobs:
            requested_time, processing_time = jobs[0]
            if requested_time == timer:
                processor.attatch_job(
                    Job(requested_time, processing_time)
                )
                jobs.pop(0)
            else:
                break

        processor.tick()
        timer += 1

    while processor.current_job or processor.jobs:
        processor.tick()

    return int(
        processor.processing_time_summed /
        processor.job_count
    )
