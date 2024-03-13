from heads_or_tails.game_engine.heads_or_tails_simple import HeadsOrTailsSimple

def main() -> None:
    num_flips = int(input("\nEnter The Number Of Coin Flips: "))

    print(f"\nFlipping A Coin {num_flips:,} Times.\n")
    
    heads_or_tails = HeadsOrTailsSimple(num_flips)

if __name__ == '__main__':
    main()

