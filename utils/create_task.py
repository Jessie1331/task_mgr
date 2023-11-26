import requests

BACKEND_URL = "http://127.0.01:5000/task"

def create_task(summary,description):
    raw_task = {
        "summary":summary,
        "description":description
    }
    response = request.post(BACKEND_URL,raw_task)
    if response.status_code == 201:
        print("Creation succeeded.")
    else:
        print("Creation failed")


if __name__ == "__main__":
    print("create a task by following the promts below:")
    summary = input("summary:")
    description = input("Description:")
    create_task(summary, description)