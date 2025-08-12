import pytest
import logging
import os
from datetime import datetime


def pytest_configure(config):
  """Configure logging to file"""
  # Tạo thư mục logs nếu chưa có
  os.makedirs("logs", exist_ok=True)
  
  # Tạo tên file với timestamp
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  log_file = f"logs/test_{timestamp}_{os.getpid()}.log"
  
  # Cấu hình logging
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
      logging.FileHandler(log_file, mode='w', encoding='utf-8'),
      logging.StreamHandler()  # Vẫn hiển thị trên console
    ]
  )
  
  # Lưu thông tin file log
  config.option.log_file = log_file
  print(f"📝 Test logs will be saved to: {log_file}")


@pytest.fixture(autouse=True)
def log_test_info(request):
  """Log test information to file"""
  test_name = request.node.name
  test_file = request.node.fspath
  
  logging.info(f"🔍 Starting test: {test_name} in {test_file}")
  
  yield
  
  logging.info(f"✅ Completed test: {test_name}")


@pytest.fixture(scope="session", autouse=True) 
def log_session_info():
  yield
