"""
Python Unpacking Examples: Nested Tuples and Sequences

This module demonstrates various unpacking techniques in Python:
1. Basic tuple unpacking
2. Nested tuple unpacking
3. Using _ for unwanted values
4. Unpacking in for loops
5. Unpacking with * (star expressions)
6. Practical real-world examples

Key Learning Points:
- Unpacking makes code more readable and Pythonic
- Use _ for values you don't need
- Nested unpacking mirrors the data structure
- Works with any iterable (lists, tuples, strings, etc.)
"""

# Sample data: metro areas with nested coordinate tuples
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def basic_unpacking_examples():
    """Demonstrate basic tuple unpacking techniques"""
    print("=== BASIC UNPACKING EXAMPLES ===\n")
    
    # Simple tuple unpacking
    point = (3, 4)
    x, y = point
    print(f"Point: {point}")
    print(f"x = {x}, y = {y}\n")
    
    # Multiple assignment (parallel assignment)
    a, b, c = 1, 2, 3
    print(f"Multiple assignment: a={a}, b={b}, c={c}")
    
    # Swapping variables (Pythonic way!)
    a, b = b, a
    print(f"After swap: a={a}, b={b}\n")

def nested_unpacking_examples():
    """Demonstrate nested tuple unpacking"""
    print("=== NESTED UNPACKING EXAMPLES ===\n")
    
    # Basic nested unpacking
    nested_data = ('Alice', (25, 'Engineer'), ('New York', 'NY'))
    name, (age, job), (city, state) = nested_data
    print(f"Name: {name}")
    print(f"Age: {age}, Job: {job}")
    print(f"Location: {city}, {state}\n")
    
    # Original metro areas example
    print("Metro areas in Western Hemisphere (longitude <= 0):")
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
    print()

def ignoring_values_examples():
    """Show how to ignore unwanted values with _"""
    print("=== IGNORING VALUES WITH _ ===\n")
    
    # Ignore middle values
    person_data = ('John', 'Doe', 30, 'Engineer', 'married')
    first, last, _, job, _ = person_data
    print(f"Employee: {first} {last}, Job: {job}\n")
    
    # Only care about name and coordinates
    print("City coordinates only:")
    for name, _, _, coordinates in metro_areas:
        lat, lon = coordinates  # Unpack the nested tuple separately
        print(f"{name}: ({lat:.2f}, {lon:.2f})")
    print()

def star_unpacking_examples():
    """Demonstrate * unpacking for variable-length sequences"""
    print("=== STAR (*) UNPACKING EXAMPLES ===\n")
    
    # Basic star unpacking
    numbers = (1, 2, 3, 4, 5, 6)
    first, *middle, last = numbers
    print(f"First: {first}")
    print(f"Middle: {middle}")
    print(f"Last: {last}\n")
    
    # Unpacking function arguments
    def greet(greeting, *names):
        return f"{greeting} {', '.join(names)}!"
    
    people = ('Alice', 'Bob', 'Charlie')
    print(greet('Hello', *people))
    
    # Dictionary unpacking
    person = {'name': 'Alice', 'age': 30}
    location = {'city': 'Boston', 'country': 'USA'}
    combined = {**person, **location}
    print(f"Combined dict: {combined}\n")

def practical_examples():
    """Real-world practical examples"""
    print("=== PRACTICAL EXAMPLES ===\n")
    
    # Processing CSV-like data
    csv_data = [
        'John,Doe,Engineer,75000',
        'Jane,Smith,Designer,68000',
        'Bob,Johnson,Manager,85000'
    ]
    
    print("Employee salary report:")
    for line in csv_data:
        first, last, position, salary = line.split(',')
        print(f"{first} {last} ({position}): ${int(salary):,}")
    print()
    
    # File path processing
    file_paths = [
        '/home/user/documents/report.pdf',
        '/var/log/system.log',
        '/etc/config/settings.conf'
    ]
    
    print("File analysis:")
    for path in file_paths:
        *directories, filename = path.split('/')
        name, extension = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        print(f"Path: {'/'.join(directories)}/")
        print(f"File: {name}.{extension}")
        print()

def enumeration_unpacking():
    """Unpacking with enumerate()"""
    print("=== UNPACKING WITH ENUMERATE ===\n")
    
    cities = ['Tokyo', 'Delhi', 'Mexico City']
    
    # Basic enumerate unpacking
    for index, city in enumerate(cities, 1):
        print(f"{index}. {city}")
    print()
    
    # Enumerate with nested data
    print("Metro areas with rankings:")
    for rank, (name, country, population, coords) in enumerate(metro_areas, 1):
        lat, lon = coords
        print(f"{rank}. {name}, {country} - Pop: {population}M - Coords: ({lat:.2f}, {lon:.2f})")
    print()

def advanced_patterns():
    """Advanced unpacking patterns"""
    print("=== ADVANCED PATTERNS ===\n")
    
    # Nested list with different structures
    mixed_data = [
        ('student', 'Alice', {'math': 95, 'science': 87}),
        ('teacher', 'Bob', {'subject': 'Physics', 'years': 10}),
        ('admin', 'Carol', {'department': 'IT', 'level': 'senior'})
    ]
    
    for role, name, details in mixed_data:
        if role == 'student':
            math_score = details['math']
            science_score = details['science']
            print(f"Student {name}: Math={math_score}, Science={science_score}")
        elif role == 'teacher':
            subject = details['subject']
            years = details['years']
            print(f"Teacher {name}: {subject}, {years} years experience")
        else:
            dept = details['department']
            level = details['level']
            print(f"Admin {name}: {dept} department, {level} level")
    print()
    
    # Unpacking return values from functions
    def get_name_and_coords():
        return 'San Francisco', (37.7749, -122.4194)
    
    city_name, (latitude, longitude) = get_name_and_coords()
    print(f"Function returned: {city_name} at ({latitude}, {longitude})")

def main():
    """Run all examples"""
    basic_unpacking_examples()
    nested_unpacking_examples()
    ignoring_values_examples()
    star_unpacking_examples()
    practical_examples()
    enumeration_unpacking()
    advanced_patterns()

if __name__ == '__main__':
    main()