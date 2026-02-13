import pandas as pd
import matplotlib.pyplot as plt

# Your data
data = {
    'year': ['1960-61', '1970-71', '1980-81', '1990-91', '2000-01', '2010-11', '2020-21', '2023-24'],
    'WestBengal': [127.5, 114.1, 96.9, 82.4, 97.5, 87.5, 82.6, 83.7],
    'Karnataka': [96.7, 101.3, 83.1, 81.1, 107.6, 115.2, 174.3, 180.7],
    'national_avg': [100, 100, 100, 100, 100, 100, 100, 100]
}

df = pd.DataFrame(data)

# Create figure with MORE SPACE at top
plt.figure(figsize=(12, 8))  # Made taller to accommodate titles

# Plot lines
plt.plot(df['year'], df['WestBengal'], 
         color='red', linestyle='--', linewidth=2.5, marker='o', 
         label='West Bengal', markersize=8)

plt.plot(df['year'], df['Karnataka'], 
         color='green', linestyle='-', linewidth=2.5, marker='s', 
         label='Karnataka', markersize=8)

plt.plot(df['year'], df['national_avg'], 
         color='gray', linestyle=':', linewidth=1.5, 
         label='National Average (100)')

# FIXED TITLES - with proper spacing
plt.suptitle('The Great Indian Reversal: 1960-2024', 
             fontsize=18, fontweight='bold', y=0.98)  # Moved UP

plt.title('How Bengal fell while Karnataka rose', 
          fontsize=14, pad=15)  # Added padding

# Labels
plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('Relative Per Capita Income (National Average = 100)', 
           fontsize=11, labelpad=10)

# Add reference line at 100
plt.axhline(y=100, color='gray', linestyle=':', alpha=0.5)

# Legend
plt.legend(loc='best', fontsize=10)

# Grid for readability
plt.grid(True, alpha=0.3)

# Add annotations with BETTER POSITIONING
plt.annotate('Bengal: 27% ABOVE', 
             xy=('1960-61', 127.5), 
             xytext=('1962-63', 140),  # Moved right
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

plt.annotate('Bengal: 16% BELOW', 
             xy=('2023-24', 83.7), 
             xytext=('2015-17', 60),  # Moved left
             arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
             fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

plt.annotate('Karnataka: 80% ABOVE', 
             xy=('2023-24', 180.7), 
             xytext=('2012-14', 195),  # Positioned higher
             arrowprops=dict(arrowstyle='->', color='green', lw=1.5),
             fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

# Extra padding to prevent cutting off
plt.tight_layout()
plt.subplots_adjust(top=0.88)  # Gives more space at top for titles

# Save with high quality
plt.savefig('india_reversal_fixed.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Fixed chart saved as 'india_reversal_fixed.png'")