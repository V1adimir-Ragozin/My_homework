import Module12_1_Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test1 = Module12_1_Runner.Runner('1')
        for i in range(10):
            test1.walk()
        self.assertEqual(test1.distance, 50)

    def test_run(self):
        test2 = Module12_1_Runner.Runner('2')
        for i in range(10):
            test2.run()
        self.assertEqual(test2.distance, 100)

    def test_challenge(self):
        test3 = Module12_1_Runner.Runner('3')
        test4 = Module12_1_Runner.Runner('4')
        for i in range(10):
            test3.walk()
            test4.run()
        self.assertNotEqual(test3.distance, test4.distance)


if __name__ == "__main__":
    unittest.main()
