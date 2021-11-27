package com.example.forecast

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import com.example.forecast.databinding.FragmentDashboardBinding

class DashboardFragment : Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val binding = DataBindingUtil.inflate<FragmentDashboardBinding>(
            inflater,
            R.layout.fragment_dashboard, container, false
        )
        binding.ourteam.setOnClickListener { view: View ->
            view.findNavController().navigate(R.id.action_dashboardFragment3_to_ourTeamFragment3)
        }
        binding.foreBtn.setOnClickListener { view: View ->
            view.findNavController().navigate(R.id.action_dashboardFragment3_to_forecastFragment)
        }
        binding.aboutBtn.setOnClickListener { view: View ->
            view.findNavController().navigate(R.id.action_dashboardFragment3_to_aboutFragment2)
        }
        setHasOptionsMenu(true)
        return binding.root
    }
}