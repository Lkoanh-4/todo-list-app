
# Danh sách để lưu các công việc
tasks = []

# Hàm thêm công việc
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task = {
        "name": task_name,
        "completed": False
    }
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")


# Hàm liệt kê tất cả công việc
def list_tasks():
    """Liệt kê tất cả công việc hiện có."""
    print("\nDANH SÁCH CÔNG VIỆC:")

    if len(tasks) == 0:
        print("Chưa có công việc nào!")
    else:
        for i in range(len(tasks)):
            if tasks[i]["completed"] == True:
                status = "[x]"
            else:
                status = "[ ]"

            print(str(i + 1) + ". " + status + " " + tasks[i]["name"])


# Hàm đánh dấu công việc hoàn thành
def complete_task(task_index):
    """Đánh dấu một công việc đã hoàn thành."""
    if task_index >= 0 and task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Đã đánh dấu công việc hoàn thành!")
    else:
        print("Chỉ số công việc không hợp lệ!")


# Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")

    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

    list_tasks()

    complete_task(0)

    list_tasks()

# Hàm xóa một công việc
def delete_task(task_index):
    """Xóa một công việc khỏi danh sách."""
    if task_index >= 0 and task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Đã xóa công việc: {deleted_task['name']}")
    else:
        print("Chỉ số công việc không hợp lệ!")
