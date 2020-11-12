using System;

namespace loan2020
{
    public class PaymentCalc
    {

        public AmortizationLine[] Schedule
        {

            get
            {
                return new AmortizationSchedule(Principal, MonthlyPayment, Months, MonthlyInterestRate).Schedule;
            }

        }


        private decimal mydecPrincipal = 100000; // this is our principal. The public property is manipulating the private variable.

        public decimal Principal // this is to define the pricinpal. 
        {
            get
            {

                return mydecPrincipal;
            }

            set
            {

                if (value > 0)
                {
                    mydecPrincipal = value;
                }

            }


        }


        private decimal mydecInterestRate = 0.06M;

        public decimal InterestRate// this is to define the Interest Rate
        {
            get { return mydecInterestRate; }
            set { if (value > 0) mydecInterestRate = value; }
        }


        private int myintMonths = 120;

        public int Months // This is to define the term 
        {
            get { return myintMonths; }
            set { if (value > 0) myintMonths = value; }
        }

        public decimal MonthlyInterestRate
        {
            get { return mydecInterestRate / 12; }

        }

        public decimal MonthlyPayment
        {
            get
            {

                decimal decBottomofFormula = (decimal)Math.Pow((double)(1 + MonthlyInterestRate), (double)Months) - 1;

                return (MonthlyInterestRate + (MonthlyInterestRate / decBottomofFormula)) * mydecPrincipal;

            }

        }


    }


    public class AmortizationLine

    {
        public AmortizationLine(decimal Principal, decimal InterestRate, decimal Payment)

        {
            myInterestPaid = Principal * InterestRate;//
            myBeginningBalance = Principal;
            myPrincipalPaid = Payment - myInterestPaid;
            myEndingBalance = Principal - myPrincipalPaid;

        }

        private decimal myEndingBalance = 0; // this is to define endlingbalance
        public decimal EndingBalance
        {
            get { return myEndingBalance; }
        }

        private decimal myBeginningBalance = 0; // this is to define beginningbalance
        public decimal BegnningBalance
        {
            get { return myBeginningBalance; }
        }

        private decimal myInterestPaid = 0;
        public decimal InterestPaid
        {
            get { return myInterestPaid; }
        }

        private decimal myPrincipalPaid = 0;
        public decimal PrincipalPaid
        {
            get { return myPrincipalPaid; }
        }

    }


    public class AmortizationSchedule

    {
        AmortizationLine[] mySchedule;
        public AmortizationSchedule(decimal Principal, decimal MonthlyPayment, int NumberOfMonths, decimal MonthlyInterestRate)
        {
            mySchedule = new AmortizationLine[NumberOfMonths + 1];
            mySchedule[0] = new AmortizationLine(Principal, 0, 0);
            for (int intMonth = 1; intMonth <= NumberOfMonths; intMonth++)
            {
                mySchedule[intMonth] = new AmortizationLine(mySchedule[intMonth - 1].EndingBalance, MonthlyInterestRate, MonthlyPayment);

            }

        }

        public AmortizationLine[] Schedule
        { get { return mySchedule; } }

    }


}