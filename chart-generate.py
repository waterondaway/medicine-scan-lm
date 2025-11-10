import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ข้อมูลตัวอย่าง
data = {
    'Model Type': [
        'Fine-Tuned with Sequence Dataset\n(Test with Sequence Data)',
        'Fine-Tuned with Shuffled Dataset\n(Test with Sequence Data)',
        'Fine-Tuned with Sequence Dataset\n(Test with Shuffled Data)',
        'Fine-Tuned with Shuffled Dataset\n(Test with Shuffled Data)'
    ],
    'F1-Score': [1.00, 0.99, 0.63, 1.00]  # กรุณาปรับค่า F1-Score ตามผลลัพธ์จริง
}

df = pd.DataFrame(data)

# ตั้งค่าธีม
sns.set(style='whitegrid')

# สร้าง Line Chart
plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df,
    x='Model Type',
    y='F1-Score',
    marker='o',
    linewidth=2.5,
    color='#4C72B0',
    markersize=10
)

# เพิ่มค่าตัวเลขบนจุด
for i, row in df.iterrows():
    offset = 0.02 if row['F1-Score'] < 0.8 else 0.01
    plt.text(
        i,
        row['F1-Score'] + offset,
        f"{row['F1-Score']:.2f}",
        ha='center',
        va='bottom',
        fontsize=10
    )

# ปรับแต่งกราฟ
plt.title('F1-Score Comparison between Fine-Tuning Approaches', fontsize=14, fontweight='bold')
plt.xlabel('Model Type', fontsize=11)
plt.ylabel('F1-Score', fontsize=11)
plt.xticks(rotation=0, ha='center', fontsize=9)
plt.ylim(0.55, 1.05)
plt.yticks([0.6, 0.7, 0.8, 0.9, 1.0])
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('f1_score_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
