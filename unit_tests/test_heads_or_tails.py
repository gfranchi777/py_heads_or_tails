from heads_or_tails.game_engine.heads_or_tails import HeadsOrTails

def main() -> None:
    num_flips = input("\nEnter The Number Of Coin Flips: ")

    heads_or_tails = HeadsOrTails(int(num_flips))

    print(f"\nFlipping A Coin {heads_or_tails.num_flips:,} Times.\n")

    heads_or_tails.flip()
    heads_or_tails.print_stats()

if __name__ == '__main__':
    main()

