from heads_or_tails.game_engine.heads_or_tails_simple import HeadsOrTailsSimple

def main() -> None:
    num_flips = input("\nEnter The Number Of Coin Flips: ")
    print("")

    heads_or_tails = HeadsOrTailsSimple(num_flips)

if __name__ == '__main__':
    main()
