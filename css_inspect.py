import re

# Define a regular expression pattern to match CSS properties
css_property_pattern = r'([a-zA-Z-]+)\s*:'

# Create a set to store unique CSS properties
unique_properties = set()

# Open the CSS file for reading
def get_unique_css_properties(css_file_path):
    with open(css_file_path, 'r') as css_file:
        # Read the CSS content
        css_content = css_file.read()

        # Use regular expression to find all CSS properties in the content
        properties = re.findall(css_property_pattern, css_content)

        # Add the unique properties to the set
        unique_properties.update(properties)

    # Convert the set to a list and return it along with the count
    return list(unique_properties), len(unique_properties)

# Replace 'styles.css' with the path to your CSS file
css_file_path = 'styles.css'
unique_properties_list, num_unique_properties = get_unique_css_properties(css_file_path)

# Print the number of unique CSS properties
print(f"Number of unique CSS properties: {num_unique_properties}")

# Print the list of unique CSS properties
print("Unique CSS Properties:")
print(unique_properties_list)
