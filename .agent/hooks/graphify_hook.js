/**
 * Graphify Automation Hook
 * Tự động kích hoạt khi có thay đổi lớn hoặc nhịp tim tổng hợp (synthesis heartbeat).
 * Vận hành dưới quyền @engineer.
 */

const { exec } = require('child_process');

function updateGraph() {
    console.log('[Graphify Hook] Đang bắt đầu cập nhật Structural Memory...');
    
    // Sử dụng --update để chỉ quét những file thay đổi, tiết kiệm token
    exec('graphify . --update', (error, stdout, stderr) => {
        if (error) {
            console.error(`[Error] Lỗi cập nhật đồ thị: ${error.message}`);
            return;
        }
        if (stderr) {
            console.warn(`[Warning] ${stderr}`);
        }
        console.log(`[Success] Đồ thị kiến thức đã được đồng bộ hóa.`);
    });
}

// Chạy ngay khi được gọi
updateGraph();
