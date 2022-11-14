let roll_value = 0
/**
 * Extensions
 * 
 * 1. show dice on LED
 * 
 * 2. Random.. tally on board of each. everyone include their 20 roll results
 * 
 * 3. Tournament - best of three - highest roll
 */
input.onGesture(Gesture.Shake, function () {
    roll_value = randint(1, 6)
    basic.showNumber(roll_value)
})
