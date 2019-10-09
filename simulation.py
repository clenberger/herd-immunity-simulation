import random
import sys
from person import Person
from logger import Logger
from virus import Virus
random.seed(42)

#testing
class Simulation(object):
    """Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when
    file is run.
    Simulates the spread of a virus through a given population.  The percentage
    of the
    population that are vaccinated, the size of the population, and the amount
    of initially
    infected people in a population are all variables that can be set when the
    program is run.
    """

    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        """
        Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of
        population vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected
        with the disease.
        The total infected people is the running total that have been infected
        since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die
        as a result
        of the infection.
        All arguments will be passed as command-line arguments when the file is
        run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        """
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding
        # parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct
        # parameters.
        # Store the array that this method will return in the self.population
        # attribute.
        # TODO: Store each newly infected person's ID in newly_infected
        # attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = None
        self.population = self._create_population(initial_infected)  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(virus_name, pop_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)
        self.newly_infected = []

    def _create_population(self, initial_infected):
        """
        This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the
                simulation
                will begin with.
            Returns:
                list: A list of Person objects.
        """
        
        initial_pop = []
        num_of_vacc_people = int(self.pop_size * self.vacc_percentage)
        num_people_left = self.pop_size - num_of_vacc_people - self.initial_infected
        
        for _ in range(0, num_of_vacc_people):
            person = Person(self.next_person_id, True, virus)
            self.next_person_id += 1
            initial_pop.append(person)
        for _ in range(self.initial_infected):
            person = Person(self.next_person_id, False, virus)
            self.newly_infected.append(person)
            initial_pop.append(person)
            self.next_person_id += 1
        for _ in range(num_people_left):
            person = Person(self.next_person_id, False, virus)
            initial_pop.append(person)
            self.next_person_id += 1
        return initial_pop
        
        # TODO: Finish this method!  This method should be called when the
        # simulation
        # begins, to create the population that will be used. This method
        # should return
        # an array filled with Person objects that matches the specifications
        # of the
        # simulation (correct number of people in the population, correct
        # percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population
        # that has
        # the correct intial vaccination percentage and initial infected.

    def _simulation_should_continue(self):
        """
        The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: True for simulation should continue, False if it should
                end.
        """
        #if self.pop_size > self.total_dead:
        #        return True
        #elif self.pop_size == self.total_dead:
        #    return False
        #elif self.pop_size == 
        #else:
        self.current_infected = len(self.newly_infected)
        if self.current_infected == 0:
            return False
        else:
            return True

            
        # TODO: Complete this helper method.  Returns a Boolean.

    def run(self):
        """
        This method should run the simulation until all requirements for ending
        the simulation are met.
        """
        
        # TODO: Finish this method.  To simplify the logic here, use the helper
        # method
        # _simulation_should_continue() to tell us whether or not we should
        # continue
        # the simulation and run at least 1 more time_step.

        # whatever = _simulation_should_continue()
        time_step_counter = 0
        
        while self._simulation_should_continue():
            self.time_step()
            time_step_counter += 1

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the
        # end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        
        while self._simulation_should_continue():
            self.time_step()
            time_step_counter += 1             
            # TODO: for every iteration of this loop, call self.time_step() to
            # compute another
            # round of this simulation.
            print('The simulation has ended after','{time_step_counter} turns.'.format(time_step_counter))
        pass

    def time_step(self):
        """
        This method should contain all the logic for computing one time step
        in the simulation.
        This includes:
            1. 100 total interactions with a random person for each infected
            person in the population
            2. If the person is dead, grab another random person from the
            population.
                Since we don't interact with dead people, this does not count
                as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
        """
        for person in self.population:
            if person.infection is True and person.is_alive is True:
                rand_people = []
                total_alive = int
                if self.pop_size - self.total_dead < 100:
                    total_alive =  self.pop_size - self.total_dead -1
                for _ in range(total_alive):
                    random_person = random.choice(self.population)
                    # evaluate if new person is dead or has an existing ID and if true, pull a new random person and append
                    while random_person.is_alive is False or random_person._id == person._id:
                        random_person = random.choice(self.population)
                    rand_people.append(random_person)
                # Run interaction
                for random_person in rand_people:
                    self.interaction(person, random_person)
                    
                did_survive = person.did_survive_infection(self.virus.mortality_rate)
                
                if not did_survive:
                    self.total_dead += 1
                    self.current_infected -= 1
                self.logger.log_infection_survival(person, did_survive)

        self._infect_newly_infected()
        

        # TODO: Finish this method.

    def interaction(self, person, random_person):
        """
        This method should be called any time two living people are selected
        for an
        interaction. It assumes that only living people are passed in as
        parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        """
        # Assert statements are included to make sure that only living people
        # are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True
        if random_person.is_vaccinated and person.infection == True:
            print("{} did not infect {}").format(person, random_person)
        if random_person.infection == True and person.infection == True:
            print("{} is already infected").format(random_person)
        if random_person.is_alive == True and random_person.is_vaccinated == False and person.infection == True:
            print("{} infected {}").format(person, random_person)
            num = random.uniform(0,1)
            if num < repro_num:
                self.newly_infected.append(random_person._id)
                random_person.infection == True
                
        self.logger.log_interaction(person, random_person)
        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0 and 1.  If that number is
        # smaller
        #     than repro_rate, random_person's ID should be appended to
        #     Simulation object's newly_infected array, so that their .infected
        #     attribute can be changed to True at the end of the time step.
        # TODO: Call logger method during this method.
        

    def _infect_newly_infected(self):
        """
        This method should iterate through the list of ._id stored in
        self.newly_infected
        and update each Person object with the disease.
        """
        for person in self.newly_infected:
            person.infection = True
            self.current_infected += 1 
        self.newly_infected = []
            
        # TODO: Call this method at the end of every time step and infect each
        # Person.
        # TODO: Once you have iterated through the entire list of
        # self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()