import os.path
import pandas as pd
from tabulate import tabulate
import pickle


def selection():
    print('Wellcome to Attrition Prediction')
    print('Choose the option')
    print('Press 1 to Upload CSV file')
    print('Press 2 to Exit')

def csv_import():
    while True:
        csv_path = input(
            "Please enter the path to the CSV file which have employee data: ")
        if csv_path.lower() == "exit":
            break
        if not os.path.exists(csv_path):
            print("File not found.")
        else:
            try:
                df = pd.read_csv(csv_path, sep=",")
                print(
                    "\nData successfully loaded from CSV file.\n\nHere are the first five rows from the CSV file.\n\n")
                # display first 5 rows of the DataFrame
                print(tabulate(df.head(),  headers='keys', showindex=False,
                      tablefmt='fancy_grid',  numalign="center", stralign="center"))
                pred_attrition(df, csv_path)
                break
            except Exception as e:
                print("An exception occurred: ", e)


def pred_attrition(df,csv_path):
    try:
        MODEL_PATH = os.path.abspath(os.path.join(
             os.path.dirname(__file__), "models", "attrition_prednew.h5"))
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
            results = model.predict(df)
            # Create a new DataFrame with the predictions
            # output_data = pd.DataFrame(results, columns=['quality'])
            df['quality_prediction'] = results
            output_data = df
            print(
                "\n\033[32mPredictions are generated successfully.\n\nHere are the first five rows from the prediction results.\n\n\033[0m")
            # display first 5 rows of the DataFrame
            print(tabulate(output_data.head(),  headers='keys', showindex=False,
                        tablefmt='fancy_grid',  numalign="center", stralign="center"))
            print("\n")
            if (filePath is not None):
                # Get the directory and base name of the input file
                input_dirname = os.path.dirname(filePath)
                input_basename = os.path.basename(filePath)

                # Create the output file path
                output_filename = os.path.join(
                input_dirname, f'{os.path.splitext(input_basename)[0]}-predictions.csv')

                # Write the output DataFrame to a CSV file
                output_data.to_csv(output_filename, index=False)

                print(
                f"\033[32m\033[1mPredictions saved to {output_filename}\033[0m\n")

    except Exception as ex:
        print(ex)
    


if __name__ == "__main__":

    option = -1

    while(True):
        selection()
        try:
            option = int(input())
        except:
            print("Your entered input is invalid. Please try again.")
        if(option == 1):
            csv_import()
        elif (option == 2):
            break
        else:
            option = 0

print("\n\033[32mThank you for Using the Attriction Predictor! \033[0m\n")