/**
 * @param {number[]} seats
 * @param {number[]} students
 * @return {number}
 */
var minMovesToSeat = function(seats, students) {
    let total=0;
    seats.sort((a, b) => a - b);
    students.sort((a, b) => a - b);

    for(let i=0;i<seats.length;i++){
        total+=Math.abs(seats[i]-students[i]);
    }
    return total;

};