from flask import Flask, jsonify, request
from sqlalchemy import and_
import os
from models import Image

app = Flask(__name__)

@app.route('/list/images', methods=['POST'])
def list_images():
    # Nhận dữ liệu JSON từ request
    json_data = request.json
    # # Khởi tạo danh sách images
    images = []

    if 'image_names' in json_data:
        name_path_list = json_data['image_names']

        # Sử dụng list comprehension để lấy tên tập tin từ mỗi đường dẫn
        image_names = [os.path.basename(path) for path in name_path_list]
        # Sử dụng câu truy vấn để lấy ra các hình ảnh từ cơ sở dữ liệu
        images = Image.query.filter(and_(Image.image_name.in_(
            image_names), Image.image_type == "STATUS_APP")).all()

    # Kiểm tra nếu có hình ảnh được trả về từ câu truy vấn
    if images:
        image_list = []
        for image in images:
            # Tạo thông tin cho mỗi hình ảnh
            image_info = {
                "id": image.id,
                "image_name": os.path.basename(image.image_path)
            }
            # Thêm thông tin hình ảnh vào danh sách
            image_list.append(image_info)

        # Trả về danh sách hình ảnh dưới dạng JSON với mã trạng thái 200
        return jsonify({"images": image_list}), 200
    else:
        # Trả về thông báo lỗi nếu không có hình ảnh nào được tìm thấy
        return jsonify({"message": "Không có hình ảnh nào được tìm thấy", "images": [], "code": 404}), 200

if __name__ == '__main__':
    app.run(debug=True)
