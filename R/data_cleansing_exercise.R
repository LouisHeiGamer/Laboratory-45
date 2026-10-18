# # 1. 建立原始資料集
raw_data <- data.frame(
  student_id = c(101, 102, 103, 104, 104, 105),
  gender = c("M", "F", "m", "F", "F", "M"),
  age = c(20, 21, 999, 19, 19, 22),  # 999 為異常值
  score = c(85, NA, 78, 92, 92, 60)  # NA 為缺失值
)

print(raw_data)


# 2. 步驟一：移除完全重複的列 (使用 unique 函數)
clean_data <- unique(raw_data)


# 3. 步驟二：將 gender 欄位統一轉為大寫 (使用 $ 符號與 toupper)
clean_data$gender <- toupper(clean_data$gender)


# 4. 步驟三：處理 age 的異常值 (大於 100 的數值轉為 NA)
clean_data$age <- ifelse(clean_data$age >100, NA, clean_data$age)

# 5. 步驟四：計算平均分數，並填補 score 欄位的缺失值 (NA)
# 先計算扣除 NA 之後的平均值
clean_mean <- mean(clean_data$score, na.rm = TRUE)

# 將 NA 填入四捨五入後的平均分數
clean_data$score <- ifelse(
  is.na(clean_data$score),
  round(clean_mean, 1),
  clean_data$score
)

# 6. 印出最終清理好的乾淨資料
print(clean_data)