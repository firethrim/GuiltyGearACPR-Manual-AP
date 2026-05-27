# GuiltyGearXXACPR-Manual-AP
A Manual APWorld for Archipelago for the fighting game Guilty Gear Accent Core Plus R

Instructions for GGXXACPR APWorld

If you don't have it, Guilty Gear Accent Core Plus R is available on steam or gog here:
https://store.steampowered.com/app/348550/GUILTY_GEAR_XX_ACCENT_CORE_PLUS_R/
It is frequently on sale for about 75% off or so (so about $3.00), so please support the developers and buy legitimate copy to play this archipelago.

Replace the save file Savedata.dat 
It should go in:
C:\Users\[username]\Documents\ARC SYSTEM WORKS\GGXXAC\save
If you have no save data already, the folder won't exist yet. This can be fixed by launching the game once first.
If you have existing save data you want to keep, back it up somewhere before overwriting it with the 100% save data.

Download the manual client here:
https://github.com/ManualForArchipelago/Manual/releases

How long to it takes to clear in a multiworld archipelago:
In my experience, it takes about 30-60 minutes per arcade clear required for the goal. So clearing 2 arcade modes in the archipelago should take about 1-2 hours. This can vary depending on the other games you are playing with and your own skill level at clearing guilty gear arcade modes.

How this archipelago is played:
You start off with one random character unlocked. You are trying to clear all 10 stages of arcade mode with a certain number of characters. Each time you clear a stage with a given character for the first time, you send a check.
There are also special condition checks for doing things like getting perfect wins or winning with full tension meter. These are also character specific.
There are also "Any Character" checks that you send the first time you achieve any of the objectives with any character. So the first time you clear stage 1 with any character, you would send the Any Character Stage 1 Win check and that specific character's Stage 1 Win check.
The default settings and restrictions that you are playing on are as follows:
	Maniac Difficulty
	Best of 3 Rounds
	No Continues allowed
	No Instant Kills allowed (as long as you have enabled the Instant Kill condition)
	No special color palettes
	No Gold Mode, Shadow Mode, or EX modes on characters are allowed
As you receive archipelago items, you will unlock or modify those restrictions.
When you clear arcade mode with a character, you are allowed to send the rest of their character specific checks if you want.
Once you have cleared arcade mode with enough characters (depending on what you set in the yaml), you are allowed to mark your victory goal as complete, finishing the game for the achipelago.

Yaml options:
Enabled Characters - Any character on this list will have items and locations associated with them included in the archipelago. You need at least 1 character for the archipelago to work. Valid Characters:
	Kliff
	Axl
	Jam
	Zappa
	Chipp
	Dizzy
	Anji
	Slayer
	ABA
	Johnny
	Millia
	Sol
	Order-Sol
	Ky
	Robo-Ky
	May
	Eddie
	Testament
	Baiken
	Venom
	Bridget
	Faust
	Potemkin
	Justice
	I-No

Enabled Conditions - Special Conditions for unlocking checks with each character. Removing a condition from this list removes all check locations related to that condition from the archipelago. Valid Conditions:
	Full Meter - Win a round while having full tension meter
	Instant Kill - Win a round by using a character's instant kill. If this is disabled, Instant Kill items are also removed from the item pool.
	Nice Burst - Whiff entirely with a burst (can't hit or be even be blocked to count. Must miss entirely)
	No Burst - Win an entire match without using any bursts
	Perfect Win - Win a round with full health. If unsure, wait to see the "Perfect" announcement at end of round
	Super Finish - Win a round by finishing your opponent with a Super Move (50% meter spending move)
	Taunt - Use a taunt in a round and still win the round

Archipelago Items -
	Characters - By default, characters are locked. You cannot use them until you have received them as an archipelago item. You start with one random character unlocked.
	Character Difficulty Reduction - By default, you play on Maniac difficulty (set in the options menu). For each Character Difficulty Reduction you have received, you are allowed to decrease the difficulty level by one step when playing as that character. 1->Very Hard, 2->Hard, 3->Normal, 4->Easy, 5->Beginner. If you find the archipelago too difficult, you are allowed to reduce the base difficulty you play at down to Very Hard and reduce from there as you receive items.
		*special note* There is a check for each character the first time you lose as them. This check will always give a difficulty reduction for that character. The logic is built around expecting the player to receive certain numbers of difficulty reductions to progress through later stages. The game does not expect the player to clear arcade mode on maniac difficulty.
	Character Gold - This unlocks the ability to use a gold mode version of a character. To select a gold mode character, use taunt to cycle through color palettes on the character select screen. When on the "Slash" palette, select the character by pressing Enemy Record. You are not required to have the Slash palette unlock to use this.
	Character Shadow - This unlocks the ability to use a shadow mode version of a character. To select a shadow mode character, use taunt to cycle through color palettes on the character select screen. When on the "Reload" palette, select the character by pressing Enemy Record. You are not required to have the Reload palette unlock to use this.
	Character EX Mode - This unlocks the ability to use a EX version of a character. To select an EX mode character, press start on the character select screen and select EX.
	Character Instant Kill - If you have the Instant Kill Condition enabled, then Instant Kills are locked for characters until you receive their specific instant kill archipelago item. Once you receive it, you may use instant kills as normal with that character.
	Character Single Round - By default, you play on best of 3 for arcade mode. If you receive this item for a character, you are allowed to (but not required to) set the rounds to 1 in options menu when playing as that character.
	Character Continue Unlock - By default, if you lose a match in arcade mode, you are not allowed to continue. If you receive this item for a character, you are allowed to use continues on that character. You are not allowed to switch characters mid way through arcade mode, but you may switch to any modes or palettes that you have unlocked for the character you are currently playing.
	Character EX Palette - Switch color palettes on the character select screen by pressing the taunt button.
	Character Slash Palette - Switch color palettes on the character select screen by pressing the taunt button.
	Character Reload Palette - Switch color palettes on the character select screen by pressing the taunt button.
	
When using the Manual client, press f1 to bring up the menu and turn off "Stop accidental button press"
You will almost certainly complete some out of logic locations at some point, and turning that off allows you to send out of logic locations.
