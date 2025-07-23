from django.db import models

# ---------- SWOT ----------
class SWOT(models.Model):
    title = models.CharField("عنوان تحلیل", max_length=200)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.title

class Strength(models.Model):
    swot = models.ForeignKey(SWOT, on_delete=models.CASCADE, related_name='strengths')
    text = models.CharField("قوت", max_length=300)
    weight = models.PositiveIntegerField("اهمیت", default=1)

    def __str__(self):
        return f"قوت: {self.text}"

class Weakness(models.Model):
    swot = models.ForeignKey(SWOT, on_delete=models.CASCADE, related_name='weaknesses')
    text = models.CharField("ضعف", max_length=300)
    weight = models.PositiveIntegerField("اهمیت", default=1)

    def __str__(self):
        return f"ضعف: {self.text}"

class Opportunity(models.Model):
    swot = models.ForeignKey(SWOT, on_delete=models.CASCADE, related_name='opportunities')
    text = models.CharField("فرصت", max_length=300)
    weight = models.PositiveIntegerField("اهمیت", default=1)

    def __str__(self):
        return f"فرصت: {self.text}"

class Threat(models.Model):
    swot = models.ForeignKey(SWOT, on_delete=models.CASCADE, related_name='threats')
    text = models.CharField("تهدید", max_length=300)
    weight = models.PositiveIntegerField("اهمیت", default=1)

    def __str__(self):
        return f"تهدید: {self.text}"


# ---------- PESTEL ----------
class PESTEL(models.Model):
    title = models.CharField("عنوان تحلیل", max_length=200)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.title

class PESTELFactor(models.Model):
    CATEGORY_CHOICES = [
        ('Political', 'سیاسی'),
        ('Economic', 'اقتصادی'),
        ('Social', 'اجتماعی'),
        ('Technological', 'تکنولوژیک'),
        ('Environmental', 'محیطی'),
        ('Legal', 'حقوقی'),
    ]
    pestel = models.ForeignKey(PESTEL, on_delete=models.CASCADE, related_name='factors')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    text = models.CharField("متن", max_length=255)
    weight = models.FloatField("وزن", default=1)

    def __str__(self):
        return f"{self.category} - {self.text}"


# ---------- PORTER ----------
class Porter(models.Model):
    title = models.CharField("عنوان تحلیل", max_length=200)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.title

class PorterFactor(models.Model):
    CATEGORY_CHOICES = [
        ('Rivalry', 'رقابت درون‌صنعت'),
        ('Suppliers', 'قدرت تأمین‌کنندگان'),
        ('Buyers', 'قدرت خریداران'),
        ('NewEntrants', 'تهدید تازه‌واردها'),
        ('Substitutes', 'تهدید محصولات جایگزین'),
    ]
    porter = models.ForeignKey(Porter, on_delete=models.CASCADE, related_name='factors')
    category = models.CharField("دسته‌بندی", max_length=20, choices=CATEGORY_CHOICES)
    text = models.TextField("توضیحات")
    weight = models.FloatField("وزن", default=1)

    def __str__(self):
        return f"{self.category} - {self.porter.title}"


# ---------- BCG ----------
class BCG(models.Model):
    title = models.CharField("عنوان تحلیل", max_length=200)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.title

class BCGItem(models.Model):
    QUADRANT_CHOICES = [
        ('Star', 'ستاره'),
        ('CashCow', 'گاو شیرده'),
        ('QuestionMark', 'علامت سؤال'),
        ('Dog', 'سگ'),
    ]
    bcg = models.ForeignKey(BCG, on_delete=models.CASCADE, related_name='items')
    name = models.CharField("نام محصول", max_length=100)
    market_growth = models.FloatField("رشد بازار")
    market_share = models.FloatField("سهم بازار")
    quadrant = models.CharField("چهارچوب", max_length=20, choices=QUADRANT_CHOICES)
    weight = models.FloatField("وزن", default=1)

    def __str__(self):
        return self.name


# ---------- ANSOFF ----------
class Ansoff(models.Model):
    title = models.CharField("عنوان تحلیل", max_length=200)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.title

class AnsoffItem(models.Model):
    STRATEGY_CHOICES = [
        ('market_penetration', 'نفوذ در بازار'),
        ('product_development', 'توسعه محصول'),
        ('market_development', 'توسعه بازار'),
        ('diversification', 'تنوع‌سازی'),
    ]
    ansoff = models.ForeignKey(Ansoff, on_delete=models.CASCADE, related_name='items')
    name = models.CharField("نام اقدام", max_length=100)
    strategy = models.CharField("استراتژی", max_length=50, choices=STRATEGY_CHOICES)
    weight = models.FloatField("وزن", default=1)

    def __str__(self):
        return self.name


# ---------- CANVAS ----------
class Canvas(models.Model):
    title = models.CharField("عنوان بوم", max_length=200)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.title

class CanvasBlock(models.Model):
    BLOCK_CHOICES = [
        ('Key Partners', 'شریک‌های کلیدی'),
        ('Key Activities', 'فعالیت‌های کلیدی'),
        ('Key Resources', 'منابع کلیدی'),
        ('Value Propositions', 'ارزش پیشنهادی'),
        ('Customer Relationships', 'روابط با مشتری'),
        ('Channels', 'کانال‌ها'),
        ('Customer Segments', 'بخش‌های مشتری'),
        ('Cost Structure', 'ساختار هزینه'),
        ('Revenue Streams', 'جریان درآمد'),
    ]
    canvas = models.ForeignKey(Canvas, on_delete=models.CASCADE, related_name='blocks')
    block_type = models.CharField("نوع بلوک", max_length=50, choices=BLOCK_CHOICES)
    content = models.TextField("محتوا")
    weight = models.FloatField("وزن", default=1)

    def __str__(self):
        return self.block_type


# ---------- VALUE PROPOSITION ----------
class ValueProp(models.Model):
    title = models.CharField("عنوان تحلیل", max_length=200)
    created_at = models.DateTimeField("تاریخ ایجاد", auto_now_add=True)

    def __str__(self):
        return self.title

class ValuePropositionItem(models.Model):
    value_prop = models.ForeignKey(ValueProp, on_delete=models.CASCADE, related_name='items')
    customer_segment = models.CharField("بخش مشتری", max_length=100)
    gains = models.TextField("دستاوردها")
    pains = models.TextField("دردها")
    products_services = models.TextField("محصولات / خدمات")
    weight = models.FloatField("وزن", default=1)

    def __str__(self):
        return self.customer_segment
