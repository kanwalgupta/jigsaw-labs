class Bundle:
    def price(self):
        if self.weight <= 5:
            return 10
        else:
            overweight = self.weight - 5
            return 10 + (overweight * 1.5)
    def processing_days(self):
        if self.dropoff_month == self.ready_month:
            return self.ready_day - self.dropoff_day
        elif (self.ready_month - self.dropoff_month) > 1:
            return (30 * (self.ready_month - self.dropoff_month - 1)) + ((30 - self.dropoff_day) + self.ready_day)
        else:
            return (30 - self.dropoff_day) + self.ready_day
    def holdingDays(self):
        if self.dropoff_month == self.pickup_month:
            return self.pickup_day - self.dropoff_day
        elif (self.pickup_month - self.dropoff_month) > 1:
            return (30 * (self.pickup_month - self.dropoff_month - 1)) + ((30 - self.dropoff_day) + self.pickup_day)
        else:
            return (30 - self.dropoff_day) + self.pickup_day
        
first_bundle = Bundle()
first_bundle.weight = 8
#print(first_bundle.price())

thirdBundle = Bundle()
thirdBundle.dropoff_month = 5
thirdBundle.dropoff_day = 29
thirdBundle.ready_month = 6
thirdBundle.ready_day = 2

# fourthBundle = Bundle()
# fourthBundle.dropoff_month = 5
# fourthBundle.dropoff_day = 29
# fourthBundle.ready_month = 7
# fourthBundle.ready_day = 2

fourthBundle = Bundle()

fourthBundle.dropoff_month = 5
fourthBundle.dropoff_day = 29
fourthBundle.ready_month = 6
fourthBundle.ready_day = 2
fourthBundle.pickup_month = 6
fourthBundle.pickup_day = 5

print(fourthBundle.holdingDays())