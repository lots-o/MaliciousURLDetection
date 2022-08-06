import numpy as np
import os
from loguru import logger
from sklearn.model_selection import train_test_split

import utils.preprocessing as p

root_dir = "./data/raw"
save_dir = "./data/preprocessing"

if not os.path.isdir(save_dir):
    logger.info(f"Make dir :: {save_dir} ")
    os.makedirs(save_dir)

logger.info("Load data...")
normal_train = p.load_csic_2010_txt(os.path.join(root_dir, "normalTrafficTraining.txt"))
normal_test = p.load_csic_2010_txt(os.path.join(root_dir, "normalTrafficTest.txt"))
anomal_test = p.load_csic_2010_txt(os.path.join(root_dir, "anomalousTrafficTest.txt"))

logger.info("Extract URL...")
normal_train = np.array([p.extract_url(request) for request in normal_train])
normal_test = np.array([p.extract_url(request) for request in normal_test])
anomal_test = np.array([p.extract_url(request) for request in anomal_test])


logger.info("Split dataset")
normal_valid, normal_test = train_test_split(
    normal_train, train_size=0.5, test_size=0.5, random_state=42, shuffle=True
)  # normalTrafficTraining -> 50%, normal validation
anomal_valid, anomal_test = train_test_split(
    anomal_test, train_size=0.5, test_size=0.5, random_state=42, shuffle=True
)  # anomalTrafficTest -> 50%, anomalTrafficValid

logger.info("Save dataset")
np.savetxt(os.path.join(save_dir, "normalTrafficTraining.txt"), normal_train, fmt="%s")
np.savetxt(os.path.join(save_dir, "normalTrafficValid.txt"), normal_valid, fmt="%s")
np.savetxt(os.path.join(save_dir, "normalTrafficTest.txt"), normal_test, fmt="%s")
np.savetxt(os.path.join(save_dir, "anomalousTrafficValid.txt"), anomal_valid, fmt="%s")
np.savetxt(os.path.join(save_dir, "anomalousTrafficTest.txt"), anomal_test, fmt="%s")
