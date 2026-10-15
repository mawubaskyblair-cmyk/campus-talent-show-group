from story import AudienceWave, TalentShow


print("=== EXTENSION 4: CANCEL THE LAST BOOKING ===")

print("Empty-show boundary case:")
empty_show = TalentShow("Victor", 3)
result = empty_show.cancel_last()
print("Expected result: False")
print("Actual result:", result)
print("Expected acts: 0")
print("Actual acts:", empty_show.act_count)
print("Expected minutes left: 3")
print("Actual minutes left:", empty_show.clock.remaining)

print("\nNormal case:")
show = TalentShow("Victor", 3)
wave = AudienceWave()

print(show.book(wave))
print("Expected acts after booking: 1")
print("Actual acts:", show.act_count)
print("Expected minutes left after booking: 2")
print("Actual minutes left:", show.clock.remaining)

result = show.cancel_last()
print("Expected cancellation result: True")
print("Actual cancellation result:", result)
print("Expected acts after cancellation: 0")
print("Actual acts:", show.act_count)
print("Expected minutes after cancellation: 3")
print("Actual minutes:", show.clock.remaining) 