
# پیش‌بینی نمره دانش‌آموز با یادگیری ماشین 🎓🤖

[🇬🇧 English](README.md)

این پروژه یک پروژه‌ی یادگیری ماشین از نوع **Regression** است که نمره نهایی دانش‌آموز را بر اساس ویژگی‌های تحصیلی و شخصی پیش‌بینی می‌کند.

## 📌 ویژگی‌های ورودی

مدل از ویژگی‌های زیر استفاده می‌کند:

- سن
- ساعات مطالعه
- درصد حضور
- نمره قبلی
- ساعات خواب
- ساعات انجام تکالیف
- فعالیت‌های فوق‌برنامه
- سطح تحصیلات والدین
- دسترسی به اینترنت

متغیر هدف:

- نمره نهایی

## 🧠 تکنولوژی‌های استفاده‌شده

در این پروژه از موارد زیر استفاده شده است:

- `Python`
- `Pandas`
- `Scikit-learn`
- `Linear Regression`
- `PolynomialFeatures`
- `pd.get_dummies()`

## 📊 دیتاست

دیتاست شامل **۱۰۰۰ رکورد مصنوعی از دانش‌آموزان** است.

ستون‌های دیتاست:

```text
id
age
study_hours
attendance
previous_score
sleep_hours
homework_hours
extracurricular
parent_education
internet_access
final_score
