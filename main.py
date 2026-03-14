import argparse
from main_bot.orders import place_market_order,place_limit_order
from main_bot.validators import validate_order
from main_bot.logs import logger

def main():
    parser=argparse.ArgumentParser(description= "BINANCE FUTURE" \
    "S TESTNET TRADING BOT")


    parser.add_argument("--symbol", required=True, help="Trading pair")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--qty", type=float, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price for LIMIT order")

    args = parser.parse_args()


    try:
                # Validate 
        validate_order(args.symbol, args.side, args.type, args.qty, args.price)

        print("\nOrder Request:")
        print(vars(args))

        # Execute 
        if args.type.upper() == "MARKET":
            response = place_market_order(
                args.symbol,
                args.side,
                args.qty
            )

        elif args.type.upper() == "LIMIT":
            response = place_limit_order(
                args.symbol,
                args.side,
                args.qty,
                args.price
            )

        # get response
        print("\nOrder Response:")
        print(response)

        # Log file
        logger.info(f"Order executed: {response}")


#exception handling
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        print("\nError:", e)


if __name__ == "__main__":
    main()
