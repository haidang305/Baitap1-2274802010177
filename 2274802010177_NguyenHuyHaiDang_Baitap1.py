import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý sinh viên")
root.geometry("600x400")

# Các nhãn và trường nhập liệu
tk.Label(root, text="Họ tên:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="MSSV:").grid(row=1, column=0, padx=10, pady=5)
entry_mssv = tk.Entry(root)
entry_mssv.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Ngày sinh:").grid(row=2, column=0, padx=10, pady=5)
entry_dob = tk.Entry(root)
entry_dob.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Lớp:").grid(row=3, column=0, padx=10, pady=5)
entry_class = tk.Entry(root)
entry_class.grid(row=3, column=1, padx=10, pady=5)

# Chức năng thêm sinh viên
def add_student():
    name = entry_name.get()
    mssv = entry_mssv.get()
    dob = entry_dob.get()
    class_ = entry_class.get()

    if name == "" or mssv == "" or dob == "" or class_ == "":
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
    else:
        tree.insert("", "end", values=(name, mssv, dob, class_))
        clear_entries()
        messagebox.showinfo("Thành công", "Đã thêm sinh viên thành công!")

# Chức năng xóa sinh viên
def delete_student():
    selected_item = tree.selection()  # Lấy mục đã chọn
    if not selected_item:  # Kiểm tra nếu không có mục nào được chọn
        messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên để xóa!")
        return
    for item in selected_item:  # Xóa các mục được chọn
        tree.delete(item)
    messagebox.showinfo("Thành công", "Đã xóa sinh viên!")
    
# Xóa thông tin trong form sau khi thêm
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_mssv.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_class.delete(0, tk.END)

# Bảng hiển thị danh sách sinh viên
tree = ttk.Treeview(root, columns=("Họ tên", "MSSV", "Ngày sinh", "Lớp"), show="headings")
tree.heading("Họ tên", text="Họ tên")
tree.heading("MSSV", text="MSSV")
tree.heading("Ngày sinh", text="Ngày sinh")
tree.heading("Lớp", text="Lớp")
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Nút thêm sinh viên
tk.Button(root, text="Thêm sinh viên", command=add_student).grid(row=4, column=0, columnspan=2, pady=10)

# Nút xóa sinh viên
tk.Button(root, text="Xóa sinh viên", command=delete_student).grid(row=6, column=0, columnspan=2, pady=10)


# Chạy vòng lặp chính
root.mainloop()

