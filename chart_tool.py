from typing import List, Dict, Union, Tuple
from dataclasses import dataclass
import plotext as plt

@dataclass
class DataPoint:
    label: str
    val: float

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, float]]) -> 'DataPoint':
        """Create a DataPoint from a dictionary with validation."""
        if not isinstance(data, dict):
            raise ValueError("Data point must be a dictionary")
        
        label = data.get('label')
        val = data.get('val')
        
        if label is None:
            raise ValueError("Missing 'label' field in data point")
        if val is None:
            raise ValueError("Missing 'val' field in data point")
            
        # Convert val to float if it's a string number
        if isinstance(val, str):
            try:
                val = float(val)
            except ValueError:
                raise ValueError(f"Invalid value '{val}' - must be a number")
                
        if not isinstance(val, (int, float)):
            raise ValueError(f"Value must be a number, got {type(val)}")
            
        return cls(str(label), float(val))

class ChartTool:
    @classmethod
    async def generate_bar_chart(cls, data: List[Dict[str, Union[str, float]]]) -> str:
        """
        Generate a bar chart from an array of data points and display it using plotext.
        
        Args:
            data: List of dictionaries containing 'label' and 'val' keys
            
        Returns:
            str: Confirmation message that chart has been generated
            
        Raises:
            ValueError: If data is invalid or empty
        """
        if not isinstance(data, list):
            raise ValueError("Data must be a list of dictionaries")
        
        if not data:
            raise ValueError("Cannot generate chart with empty data")
            
        try:
            # Convert dict data to DataPoint objects with validation
            data_points = [DataPoint.from_dict(d) for d in data]
            
            # Extract labels and values
            labels = [point.label for point in data_points]
            values = [point.val for point in data_points]
            
            # Clear any existing plots
            plt.clear_figure()
            
            # Create bar chart
            plt.bar(labels, values)
            plt.title("Bar Chart")
            
            # Show the plot
            plt.show()
            
            return "Chart has been generated and displayed to the user!"
            
        except Exception as e:
            raise ValueError(f"Error generating chart: {str(e)}")

    @classmethod
    async def generate_multiple_line_graphs(cls, data: Dict[str, Tuple[List[float], List[float]]], title: str) -> str:
        """
        Generate multiple line graphs with x and y values for each line.
        
        Args:
            data: Dictionary where keys are line labels and values are tuples of (x_values, y_values)
            title: Title of the graph
            
        Returns:
            str: Confirmation message that the graph has been generated
            
        Example:
            data = {
                "Line1": ([1, 2, 3], [10, 20, 30]),
                "Line2": ([1, 2, 3], [15, 25, 35])
            }
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        
        if not data:
            raise ValueError("Cannot generate graph with empty data")
            
        try:
            plt.clear_figure()
            
            for label, (x_values, y_values) in data.items():
                if len(x_values) != len(y_values):
                    raise ValueError(f"X and Y values must have same length for {label}")
                plt.plot(x_values, y_values, label=label)
            
            plt.title(title)
            plt.legend()
            plt.show()
            
            return "Multiple line graphs have been generated and displayed!"
            
        except Exception as e:
            raise ValueError(f"Error generating multiple line graphs: {str(e)}")

# Example usage:
# async def main():
#     chart_tool = ChartTool()
#     data = {
#         "Dataset 1": ([1, 2, 3, 4, 5], [10, 15, 7, 20, 18]),
#         "Dataset 2": ([1, 2, 3, 4, 5], [5, 12, 14, 25, 22])
#     }
#     await chart_tool.generate_multiple_line_graphs(data, "Multiple Line Plots") 