from datetime import date


start_date = date(2022, 9, 28)
end_date = date.today()
days_since = end_date - start_date
days_since = days_since.days


pills_taken = 2
pills_in_pack = 10
pack_num = 1

for i in range(days_since):

    pills_in_pack -= 1

    if pills_in_pack == 0:
        pills_in_pack = 10

num_pills = 1

print('You are on day: ', days_since, '\npills taken:', pills_taken, '\npills left in pack: ', pills_in_pack,
      '\nTake this many today: ', num_pills, '\nPack number: ', pack_num)

print(date.today())
