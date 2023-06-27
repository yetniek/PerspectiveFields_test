# import re
# import matplotlib.pyplot as plt
#
# total_loss = []
# gravity_msg_normal_loss = []
# gravity_l2_loss = []
# latitude_msg_normal_loss = []
# latitude_l2_loss = []
#
# with open('./step01-gsv-perspective-pretrain/log.txt', 'r') as file:
#     for line in file:
#         match = re.search(r'total_loss: ([\d.]+)', line)
#         if match:
#             total_loss.append(float(match.group(1)))
#
#         match = re.search(r'gravity-msg-normal-loss: ([\d.]+)', line)
#         if match:
#             gravity_msg_normal_loss.append(float(match.group(1)))
#
#         match = re.search(r'gravity-l2-loss: ([\d.]+)', line)
#         if match:
#             gravity_l2_loss.append(float(match.group(1)))
#
#         match = re.search(r'latitude-msg-normal-loss: ([\d.]+)', line)
#         if match:
#             latitude_msg_normal_loss.append(float(match.group(1)))
#
#         match = re.search(r'latitude-l2-loss: ([\d.]+)', line)
#         if match:
#             latitude_l2_loss.append(float(match.group(1)))
# # Create x-axis values (iterations)
# # Plotting the loss graphs
# plt.figure(figsize=(10, 8))
#
# # Total Loss
# # plt.subplot(1, 1, 1)
# # plt.plot(total_loss)
# # plt.title("Total Loss")
# # plt.xlabel("Iteration")
# # plt.ylabel("Loss")
#
# # Gravity Msg Normal Loss
# plt.subplot(2, 2, 1)
# plt.plot(gravity_msg_normal_loss)
# plt.title("Gravity Msg Normal Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
# # Gravity L2 Loss
# plt.subplot(2, 2, 2)
# plt.plot(gravity_l2_loss)
# plt.title("Gravity L2 Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
#
# # Latitude Msg Normal Loss
# plt.subplot(2, 2, 3)
# plt.plot(latitude_msg_normal_loss)
# plt.title("Latitude Msg Normal Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
# # Latitude Msg Normal Loss
# plt.subplot(2, 2, 4)
# plt.plot(latitude_msg_normal_loss)
# plt.title("Latitude L2 Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
#
# # Adjust layout and display the plot
# plt.tight_layout()
# plt.show()
#
# # Add legend
# plt.legend()
#
# # Display the plot
# plt.show()
import matplotlib.pyplot as plt
import re

iter_values = []
total_loss_values = []
gravity_msg_normal_loss_values = []
gravity_l2_loss_values = []
latitude_msg_normal_loss_values = []
latitude_l2_loss_values = []

# Read the log file
with open('./step01-gsv-perspective-pretrain/log.txt', "r") as file:
    log_lines = file.readlines()

# Parse the log data
for line in log_lines:
    match = re.search(r"iter: (\d+)  total_loss: ([\d.]+)  gravity-msg-normal-loss: ([\d.]+)  gravity-l2-loss: ([\d.]+)  latitude-msg-normal-loss: ([\d.]+)  latitude-l2-loss: ([\d.]+)", line)
    if match:
        iter_values.append(int(match.group(1)))
        total_loss_values.append(float(match.group(2)))
        gravity_msg_normal_loss_values.append(float(match.group(3)))
        gravity_l2_loss_values.append(float(match.group(4)))
        latitude_msg_normal_loss_values.append(float(match.group(5)))
        latitude_l2_loss_values.append(float(match.group(6)))

# Plot the loss graphs
plt.figure(figsize=(10, 6))
plt.plot(iter_values, total_loss_values, label="Total Loss")
plt.xlabel("Iteration")
plt.ylabel("Loss")
plt.title("Total Loss")
plt.savefig("Total_loss_graph.jpg")
plt.show()
plt.close()
#

# plt.figure(figsize=(12, 8))
# # Gravity Msg Normal Loss
# plt.subplot(2, 2, 1)
# plt.plot(gravity_msg_normal_loss_values)
# plt.title("Gravity Msg Normal Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
# # Gravity L2 Loss
# plt.subplot(2, 2, 2)
# plt.plot(gravity_l2_loss_values)
# plt.title("Gravity L2 Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
#
# # Latitude Msg Normal Loss
# plt.subplot(2, 2, 3)
# plt.plot(latitude_msg_normal_loss_values)
# plt.title("Latitude Msg Normal Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
# # Latitude Msg Normal Loss
# plt.subplot(2, 2, 4)
# plt.plot(latitude_l2_loss_values)
# plt.title("Latitude L2 Loss")
# plt.xlabel("Iteration")
# plt.ylabel("Loss")
#
#
# # Adjust layout and display the plot
# plt.tight_layout()
# plt.savefig("Gravity & Latitude loss_graph.png")
# plt.show()
#
#
# # Add legend
# plt.close()
