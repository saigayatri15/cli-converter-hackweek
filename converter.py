import argparse

parser=argparse.ArgumentParser(description="Convert temperature from Celsius to Fahrenheit or vice-versa")
parser.add_argument('--from',dest='from_unit',choices=['celsius', 'fahrenheit'],help="Specify the starting unit",required=True)
parser.add_argument('--to',dest='to_unit', choices=['celsius', 'fahrenheit'], help="Specify the target unit",required=True)
parser.add_argument('--value',help="Enter the temperature value",type=float,required=True)
args=parser.parse_args()
if args.from_unit=='celsius' and args.to_unit=='fahrenheit':
    convert=args.value*(9/5)+32
elif args.from_unit=='fahrenheit'and args.to_unit=='celsius':
    convert=(args.value-32)*(5/9)
else:
    convert=args.value
print(f"{args.value} ° {args.from_unit.capitalize()} = {round(convert,2)} ° {args.to_unit.capitalize()}") 