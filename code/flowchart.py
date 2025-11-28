import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Setup the figure
fig, ax = plt.subplots(figsize=(15, 8))
ax.set_xlim(0, 15)
ax.set_ylim(0, 10)
ax.axis('off')

# Define standard box dimensions and spacing based on friend's diagram
box_width = 1.8
box_height = 0.8
h_spacing_short = 0.6 # Short horizontal spacing
h_spacing_long = 1.2 # Longer spacing for connections
v_spacing_down = 2.0 # Vertical spacing down for main flow

# Y coordinates for rows
row1_y = 6.0
row2_y = 3.0

# --- Row 1: Data to Hybrid Model ---

# 1. Data Set (Cylinder shape)
data_set_x = 1.0
data_set_center = (data_set_x, row1_y)
cylinder = patches.Ellipse(data_set_center, box_width * 0.8, box_height * 1.5, fc='white', ec='black', lw=1.5, angle=0)
ax.add_patch(cylinder)
ax.text(data_set_center[0], data_set_center[1], "Data Set\n(Raw Movies, Ratings)", ha='center', va='center', fontsize=9, fontweight='bold')

# 2. Data Pre-Processing
preprocess_x = data_set_x + box_width/2 + h_spacing_short + box_width/2
preprocess_center = (preprocess_x, row1_y)
rect1 = patches.Rectangle((preprocess_center[0]-box_width/2, preprocess_center[1]-box_height/2), box_width, box_height, fc='white', ec='black', lw=1.5)
ax.add_patch(rect1)
ax.text(preprocess_center[0], preprocess_center[1], "Data Pre-Processing", ha='center', va='center', fontsize=9, fontweight='bold')

# 3. Feature Extraction (Sentifusion)
feature_x = preprocess_x + box_width/2 + h_spacing_short + box_width/2
feature_center = (feature_x, row1_y)
rect2 = patches.Rectangle((feature_center[0]-box_width/2, feature_center[1]-box_height/2), box_width, box_height, fc='white', ec='black', lw=1.5)
ax.add_patch(rect2)
ax.text(feature_center[0], feature_center[1], "Feature Extraction\n(Sentifusion)", ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(feature_center[0], feature_center[1]-0.3, "(VADER, Weighted Rating)", ha='center', va='center', fontsize=7, color='gray')


# 4. Create Hybrid Model (The Ensemble)
hybrid_x = feature_x + box_width/2 + h_spacing_short + box_width/2
hybrid_center = (hybrid_x, row1_y)
rect3 = patches.Rectangle((hybrid_center[0]-box_width/2, hybrid_center[1]-box_height/2), box_width, box_height, fc='white', ec='black', lw=1.5)
ax.add_patch(rect3)
ax.text(hybrid_center[0], hybrid_center[1], "Create Hybrid\nEnsemble Model", ha='center', va='center', fontsize=9, fontweight='bold')


# 5. Base ML Models (CBF & CF) - This is a conceptual box, like friend's
ml_models_x = hybrid_x + box_width/2 + h_spacing_short + box_width/2
ml_models_center = (ml_models_x, row1_y)
circle2 = patches.Ellipse(ml_models_center, box_width * 0.8, box_height * 1.5, fc='white', ec='black', lw=1.5) # Similar to friend's ML Models
ax.add_patch(circle2)
ax.text(ml_models_center[0], ml_models_center[1], "Base ML Models\n(CBF & CF)", ha='center', va='center', fontsize=9, fontweight='bold')

# --- Row 2: Evaluation and Feedback Loop ---

# 6. Train with Hybrid Model (Implicitly means apply to data)
train_x = ml_models_x
train_center = (train_x, row2_y)
rect4 = patches.Rectangle((train_center[0]-box_width/2, train_center[1]-box_height/2), box_width, box_height, fc='white', ec='black', lw=1.5)
ax.add_patch(rect4)
ax.text(train_center[0], train_center[1], "Apply Hybrid Model\nfor Recommendations", ha='center', va='center', fontsize=9, fontweight='bold')


# 7. New Data (Decision shape, like friend's)
new_data_x = train_x - box_width/2 - h_spacing_long - box_width/2
new_data_center = (new_data_x, row2_y)
diamond = patches.RegularPolygon(new_data_center, numVertices=4, radius=box_height*0.7, fc='white', ec='black', lw=1.5)
ax.add_patch(diamond)
ax.text(new_data_center[0], new_data_center[1], "New Data\n/Feedback", ha='center', va='center', fontsize=9, fontweight='bold')

# 8. Result Analysis & Evaluation
results_x = new_data_x - box_width/2 - h_spacing_long - box_width/2
results_center = (results_x, row2_y)
rect5 = patches.Rectangle((results_center[0]-box_width/2, results_center[1]-box_height/2), box_width, box_height, fc='white', ec='black', lw=1.5)
ax.add_patch(rect5)
ax.text(results_center[0], results_center[1], "Result Analysis\n& Evaluation", ha='center', va='center', fontsize=9, fontweight='bold')
ax.text(results_center[0], results_center[1]-0.3, "(RMSE, Precision, Recall)", ha='center', va='center', fontsize=7, color='gray')


# --- Arrows ---

# Arrow properties matching friend's diagram (simpler heads)
arrow_props_straight = dict(arrowstyle="->", connectionstyle="arc3,rad=0", fc='black', ec='black', lw=1.5, shrinkA=0.05, shrinkB=0.05)
arrow_props_vertical = dict(arrowstyle="->", connectionstyle="arc3,rad=0", fc='black', ec='black', lw=1.5, shrinkA=0.05, shrinkB=0.05)
arrow_props_curved_down = dict(arrowstyle="->", connectionstyle="arc3,rad=0.3", fc='black', ec='black', lw=1.5, shrinkA=0.05, shrinkB=0.05) # For a smoother turn


# Row 1 Horizontal Arrows
ax.annotate("", xy=(preprocess_center[0]-box_width/2, row1_y), xytext=(data_set_center[0]+box_width*0.4, row1_y), arrowprops=arrow_props_straight)
ax.annotate("", xy=(feature_center[0]-box_width/2, row1_y), xytext=(preprocess_center[0]+box_width/2, row1_y), arrowprops=arrow_props_straight)
ax.annotate("", xy=(hybrid_center[0]-box_width/2, row1_y), xytext=(feature_center[0]+box_width/2, row1_y), arrowprops=arrow_props_straight)
ax.annotate("", xy=(ml_models_center[0]-box_width*0.4, row1_y), xytext=(hybrid_center[0]+box_width/2, row1_y), arrowprops=arrow_props_straight)

# Vertical arrow from ML Models to Train
ax.annotate("", xy=(train_center[0], train_center[1]+box_height/2), xytext=(ml_models_center[0], ml_models_center[1]-box_height*0.75), arrowprops=arrow_props_vertical)

# Row 2 Horizontal Arrows
ax.annotate("", xy=(new_data_center[0]+box_height*0.7, row2_y), xytext=(train_center[0]-box_width/2, row2_y), arrowprops=arrow_props_straight) # From Train to New Data
ax.annotate("", xy=(results_center[0]+box_width/2, row2_y), xytext=(new_data_center[0]-box_height*0.7, row2_y), arrowprops=arrow_props_straight) # From New Data to Results

# Feedback loop from Results back to Data Set (implied re-training/update)
ax.annotate("", xy=(data_set_center[0]-box_width*0.4, row1_y),
            xytext=(results_center[0]-box_width/2, row2_y),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.5", fc='black', ec='black', lw=1.5, shrinkA=0.05, shrinkB=0.05))


# Title
plt.title('Model FrameWork: Sentifusion-Enhanced Hybrid Movie Recommender System', fontsize=16, pad=20)

plt.savefig('workflow_diagram_exact_friend_style.png')
print("workflow_diagram_exact_friend_style.png")