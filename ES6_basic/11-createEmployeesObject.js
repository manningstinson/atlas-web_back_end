export default function createEmployeesObject(departmentName, employees) {
  const departmentObject = {};
  departmentObject[departmentName] = employees;
  return departmentObject;
}

const departmentName = ' ';
const employees = ['John', 'Alice', 'Bob'];

const employeesObject = createEmployeesObject(departmentName, employees);
console.log(employeesObject); // Output: { ' ': ['John', 'Alice', 'Bob'] }
