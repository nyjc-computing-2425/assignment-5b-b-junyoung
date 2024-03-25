# Part 1
def read_csv(filename):
  """
  Reads data from a CSV file and returns a header as a list and the data as a nested list.

  Parameters
  ---------
  filename: str
      contains the CSV file to be read

  Returns
  ---------
  two lists
      contains the header and the data respectively
  """
  header = []
  data = []

  with open(filename, 'r') as file:
      lines = file.readlines()

  header = lines[0].strip().split(',')

  for line in lines[1:]:
      row = line.strip().split(',')
      converted_row = []
      for item in row:
          try:
              converted_item = int(item)
          except ValueError:
              try:
                  converted_item = float(item)
              except ValueError:
                  converted_item = item
          converted_row.append(converted_item)
      data.append(converted_row)

  return header, data

# Part 2
def filter_gender(enrolment_by_age, sex):
  """
  Takes a list of records: enrolment_by_age and returns a list of records where "sex" column is excluded.

  Parameters
  ---------
  enrolment_by_age: list, sex: str
    enrolment_by_age is the list of records
    string sex is the string used to find the "sex" column
      

  Returns
  ---------
  list
      a list with three columns: year, age, and enrolment_jc

  Example:
  >>> mf_enrolment = filter_gender(enrolment_data, "MF")
>>> mf_enrolment
[[1984, '17 YRS', 8710],
 [1984, '18 YRS', 3927],
 [...],
 [...],
 ...]
  """
      # Type your code below
  filtered_records = []
  header, data = read_csv('pre-u-enrolment-by-age.csv')
  for line in data:
      if sex in line:
          line.pop(2)
          filtered_records.append(line)
  return filtered_records

# Part 3
def sum_by_year(enrolment_data):
  """
  Adds up the total enrolment for each year, regardless of age
and returns the result as a list of lists.

  Parameters
  ---------
  enrolment_data: int
      the value to be summed to find total enrolment

  Returns
  ---------
  list
      a nested list where each inner list comprises two integers, year and total_enrolment


  Example:
  >>> enrolment_by_year = sum_by_year(mf_enrolment)
>>> enrolment_by_year
[[1984, 21471],
 [1985, 24699],
 [...],
 [...],
 ...]
  """
    # Type your code below
  enrolment_final_data = []
  years_enrolment = {}
  
  for line in enrolment_data:
      year = line[0]
      enrolment = line[2]
      if year in years_enrolment:
          years_enrolment[year] += enrolment
      else:
          years_enrolment[year] = enrolment

  for year, enrolment in years_enrolment.items():
      enrolment_final_data.append([year, enrolment])
  
  enrolment_final_data.sort()
  
  return enrolment_final_data

# Part 4
def write_csv(filename, header, data):
  """
  Writes header and data to filename in CSV format and returns the number of lines written.

  Parameters
  ---------
  header: list, data: list, filename: str
      header is the list containing the column labels
      data is the nested list containing the data
      filename is the string that contains the CSV file

  Returns
  ---------
  int
      the number of lines written to the CSV file

  Example:
>>> filename = 'total-enrolment-by-year.csv'
>>> header = ["year", "total_enrolment"]
>>> write_csv(filename, header, enrolment_by_year)
35
  """
    # Type your code below
  with open(filename, 'w') as f:
    f.write(','.join(header))
    f.write('\n')

    for row in data:
        f.write(','.join(map(str, row)))
        f.write('\n')

    return len(data) + 1 